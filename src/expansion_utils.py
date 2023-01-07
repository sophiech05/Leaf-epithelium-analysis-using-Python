 # Imports

import tifffile
from scipy import ndimage as ndi
import skimage
import numpy as np
import napari
from typing import List
from magicgui import magicgui
from napari.types import ImageData, LabelsData, LayerDataTuple
import numpy as np
import glob
import os
import pandas as pd
from skimage import measure
import pandas as pd
from skimage.morphology import convex_hull_image
import matplotlib.pyplot as plt
from skimage.measure import regionprops_table
from skimage.util import map_array

# Settings of the MASK images: change the numbers to get the correct segmentation
local_threshold_block_size = 100
area_threshold = 400
radius_disk_closing = 2
radius_disk_opening = 6
min_size_object = 150

 # Get the MASK images

def create_label(filename):
    
    #load image
    img = tifffile.imread(filename)
    img=img[:,:,0]
    
    # Apply filter
    img = skimage.filters.gaussian(img, sigma=1, mode="nearest")
    
    # Create treshold 
    local_threshold = skimage.filters.threshold_local(img, block_size=151)
    mask = img > local_threshold

    # Post process : binary_closing and binary_opening
    mask = skimage.morphology.binary_closing(
        mask, skimage.morphology.disk(radius_disk_closing))

    mask = skimage.morphology.remove_small_holes(
        mask, area_threshold)

        # Remove small objects
    mask = skimage.morphology.remove_small_objects(
        mask, min_size_object)

    mask = skimage.morphology.binary_opening(
        mask, skimage.morphology.disk(radius_disk_opening))
    
    mask_label = skimage.morphology.label(mask)
    return mask_label



 # Calculate the convexhull perimeter
    
def convexhull_perimeter(regionmask):                 
    convex_hull = convex_hull_image(regionmask)
    perimeter = measure.perimeter(convex_hull)
    return perimeter



 # Funcion to create a dataframe with area, perimeter and convexhull perimeter 
    
def measure_species(mask_path, species_name):          
    df = pd.DataFrame()
    for image in glob.glob(mask_path + "/*.tif"):       # Open all the image.tif
     
        mask_img = tifffile.imread(image)
        mask_img = skimage.morphology.label(mask_img)   # get the labelled mask
    
        table = measure.regionprops_table(
            mask_img,                                   # label corresponding to our mask
            properties=('label',"area","perimeter"),    # get the area and perimeter of the cells
            extra_properties=(convexhull_perimeter,) )  # get the convex hull perimeter
        
        df2= pd.DataFrame(table)
        df= pd.concat([df,df2])
        df = df.assign(lobeyness = df["perimeter"]/df["convexhull_perimeter"])  # Calculate the lobeyness

    df = df.assign(species = f'{species_name}')         # Add a column with the name of the corresponding species
    df = df.reset_index(drop=True)
    return df

