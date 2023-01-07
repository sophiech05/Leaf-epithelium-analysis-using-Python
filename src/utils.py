import tifffile
from scipy import ndimage as ndi
import skimage
from skimage.measure import label
from skimage import measure
import numpy as np
import napari
from typing import List
from magicgui import magicgui
from napari.types import ImageData, LabelsData, LayerDataTuple, PointsData
import glob
import pandas as pd
import os
import csv
from skimage.segmentation import watershed
from sklearn.neighbors import NearestNeighbors
from junction_finder import *

#functions to save the identified centroids or junctions into .csv formats

def save_data(filename, centroid_pos):
    header = ['image_fname', 'nb_cells', 'centroids_fname']
    if not os.path.isfile('how_many_cells_database.csv'):
        with open('how_many_cells_database.csv', 'x') as csvfile:  #checking if the file exist to create it if not
            writer = csv.DictWriter(csvfile, fieldnames=header)    
            writer.writeheader()  
    
    df = pd.read_csv("how_many_cells_database.csv")
    # updating the column value/data
    df.loc[filename+'.tif'] = [filename+'.tif',len(np.unique(centroid_pos))//2, "cells_centroid-"+filename+'.csv']
    # writing into the file
    df.to_csv("how_many_cells_database.csv", index=False)
    
def save_junction_data(filename, junction_number):
    header = ['image_fname', 'nb_non_triangular_junctions', 'non_triangular_junctions_fname']
    if not os.path.isfile('non_triangular_junctions_database.csv'): 
        with open('non_triangular_junctions_database.csv', 'x') as csvfile:  #checking if the file exist to create it if not
            writer = csv.DictWriter(csvfile, fieldnames=header)    
            writer.writeheader()  
    
    df = pd.read_csv("non_triangular_junctions_database.csv")
    # updating the column value/data
    df.loc[filename+'.tif'] = [filename,junction_number, "non_triangular_junctions-"+filename+'.csv']
    # writing into the file
    df.to_csv("non_triangular_junctions_database.csv", index=False)
    
def save_centroids(filename, centroids):
        centroids = centroids[1:]
        if not os.path.isfile(filename+'.csv'):  #check if the file exist, to print a warning and pass if the case
            with open(filename+'.csv', 'x') as csvfile: #create the file
                centroids.to_csv(filename+'.csv', mode='a', index=True) #write the dataframe into it
        else:
            print(f'a csv for {filename} already exists')
            return
        
def save_junction_pos(filename, junctions):
        if not os.path.isfile(filename+'.csv'): #checking if the file exist to create it if not
            with open(filename+'.csv', 'x') as csvfile: #create the file
                junctions.to_csv(filename+'.csv', mode='a', index=True) #write the dataframe into it
        else:
            print(f'a csv for {filename} already exists')
            return

#a function to get all tif files from a directory given by the user
def get_path():
    print('Please put below the directory of the folder containing your images of interest: ')
    tmp = input()
    fnames = glob.glob(tmp+'/*.tif')
    return fnames

fnames = get_path()

#all widgets for napari

#simple widget to allow user to open an image from the directory
@magicgui(
    fname={"choices": fnames}
) 
def get_image(
    fname=fnames[0]
    ) -> LayerDataTuple:

    raw = tifffile.imread(fname)
    
    return [(raw[:,:,0], {"name":"raw",'colormap':'gray'}, "image"),]

#widget to perform processing operations resulting in the segmentation of the cells
@magicgui(
    filter_type= {"choices": ["gaussian", "median","no filter"]},
    slider={"widget_type": "FloatSlider", 'max': 10},
    mode={"choices": ["reflect", "constant", "nearest", "mirror", "wrap"]},
) 
def processing(
    img: ImageData, 
    filter_type, 
    slider: float = 1.0, 
    mode = "nearest", 
    local_threshold_block_size:int=150,
    radius_disk_closing:int=1,
    radius_disk_opening:int=8,
    min_size_object:int=150,
    )-> LabelsData:
    
    if filter_type == "gaussian":   #an option for the user to apply preprocessing filter to their image
        img =  skimage.filters.gaussian(img, sigma=slider, mode=mode)
    elif filter_type == "median":
        footprint = skimage.morphology.disk(slider) 
        img = skimage.filters.median(img, footprint = footprint, mode = mode)

    if local_threshold_block_size%2 == 0: #threshold operation to highlight part of the image
        local_threshold_block_size+=1
    local_threshold = skimage.filters.threshold_local(img, block_size=local_threshold_block_size)
    mask = img > local_threshold
    
    mask = skimage.morphology.binary_closing(                  #series of morphology operation to isolate cell shapes
        mask, skimage.morphology.disk(radius_disk_closing))
    
    mask = skimage.morphology.remove_small_holes(
        mask, area_threshold=400)

    # Remove small objects
    mask = skimage.morphology.remove_small_objects(
        mask, min_size_object)

    mask = skimage.morphology.binary_opening(
        mask, skimage.morphology.disk(radius_disk_opening))
    
    labeled = label(mask)
        
    return labeled

#widget to identify centroid of cells from an already segmented image
@magicgui(
    fname={"choices": fnames}
) 
def centroid(
    fname,
    label_objects:LabelsData,
    ) -> PointsData:    
    fname = os.path.splitext(os.path.basename(fname))[0]
    props = measure.regionprops_table(
    label_objects,
    properties=['label', 'centroid'] # properties to be measured
    )
    
    df_props = pd.DataFrame(props)   # transform into panda table
    df_props.columns = ['label', 'axis-0', 'axis-1']
    # show centroids on the viewer
    centroids = df_props[['axis-0','axis-1']]
    save_centroids("cells_centroid-"+fname, centroids)
    save_data(fname,centroids)
    return centroids

#widget to return a skeleton of an already segmented image
@magicgui 
def skeleton(
    segmentation:LabelsData,
    ) -> LabelsData:
    
    erod = skimage.morphology.binary_erosion(
        segmentation, skimage.morphology.disk(5))
    
    labeled = label(erod)
    
    elev_map = np.ones(labeled.shape, dtype=int)
    
    final = watershed(elev_map,labeled,watershed_line=True)
    final = final < 1 #the idea is to perform a watershed with the segmentation and use the separation line as a skeleton
    return final

#widget to identify and return non triangular junctions from a skeleton
@magicgui(
    fname={"choices": fnames}
) 
def junctions(
    fname,
    skeleton:LabelsData,
    ) -> PointsData:
    
    shape = skeleton.shape
    
    input_image = skeleton.astype(np.uint8) #requirement for the hit or miss function we will use to identify junctions
    
    intersections = find_line_intersection(input_image, 0)
    intersections.astype(int)
    
    #we are going to scout 20 by 20 pixels around the intersections to count how many time it crosses with the skeleton
    points = np.nonzero(intersections)
    triangulars = []
    out = []
    for i in np.transpose((points[0], points[1])):
        if i[0]-10 > 0 and i[1]-10 > 0 and i[0]+10 < shape[0] and i[1]+10  < shape[1]:
            outer = skeleton[max(0,i[0]-10):min(i[0]+10,shape[0]),max(0,i[1]-10):min(i[1]+10,shape[1])] #[i[0]:i[0]+5,i[1]:i[1]+5]
            inner = skeleton[max(0,i[0]-9):min(i[0]+9,shape[0]),max(0,i[1]-9):min(i[1]+9,shape[1])]
            inner = np.pad(inner, 1, mode='constant', constant_values=0)
            outer = outer - inner
            #print(label(outer))
            if len(np.unique(label(outer))) > 3: #with hindsight this entire part of the function is more useful to find non triangular junctions, all junctions are already triangular by nature....
                triangulars.append(i)
                    
    nearest = NearestNeighbors(n_neighbors= 2, algorithm= "ball_tree").fit(triangulars) #so here another, more precise way to identify non triangular junctions using standard neearestneighbor algo
    distances = nearest.kneighbors(triangulars)[0]
    distances = distances[:,1]
    
    for i in range(0,len(distances)):
        if distances[i] < 10 :
            out.append(triangulars[i])
            
    nb_junction = len(out)
    df_junction = pd.DataFrame(out, columns = ['axis-0','axis-1']) #create a dataframe containing the pos of all the junctions
    fname = os.path.splitext(os.path.basename(fname))[0]
    save_junction_data(fname,nb_junction)
    save_junction_pos("non_triangular_junctions-"+fname, df_junction)
    return out