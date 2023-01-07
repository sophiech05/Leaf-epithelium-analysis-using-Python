# Leaf epithelium analysis using Python


6 January 2023
Sara Hervada, Antoine Babu, Sophie Chavigny

Keywords: Epithelia, Plant, Image Processing, Napari, Computational Biology, Systems Biology, Cell Biology

## Introduction 

Leaf epithelia are significant plant tissues because they protect the leaf surface and are essential for the flow of gasses and water within the plant. According to Sapala et al. 2018, the mechanics of leaf growth are connected to the wide variety of cell shapes found in leaf epithelia. In leaf epithelia, we may learn about the structure, function, and development of the tissue by examining the cell shape.
When examining leaf epithelia, image analysis techniques are especially helpful since they make it possible to extract specific information from photographs of the cells more quickly than if one does it manually. 

In this project we aim to better comprehend leaf epithelia and provide answers to crucial questions by developing an image analysis pipeline and utilizing Python to examine the data. Given that the cells in epithelial tissue can have complicated and changeable forms, it can be challenging to precisely segment epithelial tissues as the cells frequently overlap or are partially covered by other cells or structures, such as stomatal pores or vein leaves. Moreover, images can have different quality, exposure and contrast, which can also be problematic in some cases. 

Our goal is to create a pipeline that allows us to process different epithelia images making simple parameter adjustments in response to variations in the given image.



### Definitions :

- **Turgor pressure** : the internal pressure within the cell that pulls the plasma membrane against the cell wall. Turgor pressure within cells is regulated by osmosis, and leads to the expansion of the cell wall during growth.
- **Abaxial / adaxial** : the upper and bottom sides of a leaf and the inner and outer sides of the floral organs, respectively, are represented by the adaxial and abaxial sides. On the adaxial and abaxial sides of lateral organs, there are two cell populations with differing histological characteristics.
- **Epidermis, epithelium** : The epidermis is the outermost of the three layers that make up the skin; the interior layers are the dermis and hypodermis. 
The epithelium is the thin tissue forming the outer layer of a body's surface and lining the alimentary canal and other hollow structures.
- **Microtubule** : tubulin polymers that make up the cytoskeleton, which gives eukaryotic cells their shape and organization.
- **Toluidine blue staining** : a basic thiazine metachromatic dye that has a strong affinity for the acidic tissue constituents found in DNA and RNA-rich tissues.
- **Cell wall / membrane** : A cell wall is a rigid layer of polysaccharides that is present outside the plasma membrane of bacteria, fungi, and plant cells. It is primarily composed of cellulose in algae and higher plants.
A cell membrane, also known as a plasma membrane, and made of semipermeable lipid bilayer, separates the interior of the cell from the external environment and controls the movement of materials into and out of the cell. 


## Python dependencies
List of libraries / modules that are required to run our code:


- `Pandas`
- `Matplotlib`
- `Napari`
- `Magicgui`
- `Skimage`
- `Numpy`
- `Tifffile`
- `Glob`
- `Seaborn`
- `Sklearn`
- `CV2`


## HOW MANY CELLS?

### How to use
This code will allow you to count the number of cells present on your microscopic photograph and to determine their positions. 
Here is how to use this code: 

0) Download the folder `how_many_cells.zip`. 
You will find files `utils.py`, `how_many_cells.ipynb`, and a folder with images we worked on. 

1) Using your terminal, launch the Jupyter Notebook and open the Notebook `how_many_cells.ipynb`.
2) Run the first block of the code. You will have to enter 2 times the path leading to the images we want to process. You must enter the full path, depending on where you put your `how_many_cells` folder. The following is an example of what you should enter: 
/Users/chavignysophie/Desktop/Bioinfo_project/how_many_cells/images
<img width="729" alt="Capture d’écran 2023-01-05 à 21 10 23" src="https://user-images.githubusercontent.com/122089106/210978454-7037d522-0c66-491e-af8e-76af39b628ed.png">

If your path is correct, you will see the following output:
<img width="1203" alt="Capture d’écran 2023-01-06 à 10 56 31" src="https://user-images.githubusercontent.com/122089106/210978658-9bd5bb92-315c-4104-ab47-acb8b665d863.png">

3) Now, run the 2nd window of code to open the Napari Viewer. Your Napari Viewer should open.
<img width="525" alt="Capture d’écran 2023-01-06 à 10 56 35" src="https://user-images.githubusercontent.com/122089106/210978749-e4abc90b-69d8-4e08-8002-71ff906d8eca.png">

Then, run the last block of code in order to obtain the necessary widgets in your Napari:
<img width="1440" alt="Capture d’écran 2023-01-06 à 10 53 11" src="https://user-images.githubusercontent.com/122089106/210978989-326a4395-3e06-4b96-ab3d-fc6175dc0ae3.png">

4) Using the first widget, choose the image you want to analyze and click run.
<img width="970" alt="Capture d’écran 2023-01-06 à 10 57 01" src="https://user-images.githubusercontent.com/122089106/210979094-8146d0ce-d0b1-4bbe-9790-eb578dd39c45.png">
<img width="1420" alt="Capture d’écran 2023-01-06 à 10 49 30" src="https://user-images.githubusercontent.com/122089106/210979606-8e00e5be-923f-4890-b1af-20cfd88a793e.png">


5) Using the second widget, click on run and create a mask for your image. This mask should cover and label in different colors the cells you want to count. If the mask seems strange and does not label the cells correctly, you can play around with different parameters of the widget. For example, if your image has many very small cells you want to count, set min size objects at 0. 
The mask should ideally look like this: 
<img width="1436" alt="Capture d’écran 2023-01-06 à 10 51 48" src="https://user-images.githubusercontent.com/122089106/210979727-7078b972-33cd-484f-9704-45ecafd6f888.png">


Tip: if there are some labels that do not represent cells and are not able to better it by varying parameters, you can delete them manually. Click on “fill” and chose label 0, then delete the label simply by clicking on it on the image: 

<img width="249" alt="Capture d’écran 2023-01-06 à 10 52 55" src="https://user-images.githubusercontent.com/122089106/210979920-edff4689-fcad-48fb-a9b5-60ffdfc66b19.png">


6) When your mask seems good, use the last widget in order to count the cells and find their positions (centroids) by clicking on the run button. Do not forget to choose the right path according to the image you are processing, otherwise the data won’t be stored correctly.
<img width="1440" alt="Capture d’écran 2023-01-06 à 10 52 01" src="https://user-images.githubusercontent.com/122089106/210979971-d2141e07-2581-4895-af01-e2818cc7c57f.png">


7) Repeat this with all the images you want to analyze.
8) When you are done, all the results are collected in the folder `how_many_cells`. 
You will see one csv file that summarizes all your results (name of the image, number of cells counted, name of the csv file with the positions of the cells/their centroids) and csv files with the positions of the cells/their centroids for each processed image.
This will look like this:  
<img width="792" alt="Capture d’écran 2023-01-06 à 10 57 11" src="https://user-images.githubusercontent.com/122089106/210980393-c86f0c72-3236-4f6c-ba73-366d38238b6a.png">


### Limitations 

- The segmentation of some images is still not perfect even after changing characteristics. We can correct the mask manually but this takes time.
- In the `global_cell_count.csv` file created automatically, the column with the file names is missing and we should add it manually, which is also time consuming and therefore has to be improved.
- We can consider improve the code so it can create automatically an additional folder `results_per_image` in which will be saved all the csv files with the positions of the cells (instead of them be stored just next to the `global_cell_count.csv` file). This will make the interpretation of the results easier and clearer. 

---------------------------------

## CELL EXPANSION
Using this code, you may examine the growth of the cells seen on your microscopic image by calculating their "lobeyness," which is the deviation of 2D cell contours from the shapes of typical undifferentiated cells.

### How to use

0) Download the folder `cell_expansion.zip`. 
You will find files `utils.py`, `cell_expansion.ipynb`, and a folder with images we worked on. 

1) Using your terminal, launch the Jupyter Notebook and open the Notebook `cell_expansion.ipynb`.
2) Run the first block of the code in order to import all the imports needed, indicated in the jupyter notebook.

3) Determine the mask of each image using the create_label function and running this code, after indicating the correct path to the pictures
4) Store the mask by species (one folder for each species).
5) Run the `convexhull_perimeter` function.
6) Run the `measure_species` function, indicating the correct path to the species containing the mask images and the name of the corresponding species. 
→ You will get for each species a dataframe with all the data needed to study its cell expansion.
7) Concatenate all the data frame into a one single one  

![image1](https://user-images.githubusercontent.com/122090278/211149641-d1e25eae-f0f2-4b92-a280-a846d32d087e.png)


8) Run the code for the violin plot!

![figure_6 A](https://user-images.githubusercontent.com/122090278/211149667-179c8d4a-86b2-437d-a73c-4c9ed739fdcb.png)


9) Run the code for the scatter plot

![figure_6 B](https://user-images.githubusercontent.com/122090278/211149668-3021fccf-11ee-491f-b96b-33762d06a055.png)


10) To verify our plots, we run the code to create a parametric map

![image4](https://user-images.githubusercontent.com/122090278/211149597-6f9be029-1939-4b85-9818-4adcea4ae64c.png)



### Limitations 
- The masked images appear beside the original images. We have to manually move the masked images into their respective folder, organized according to their species. We can consider improving the code adding a .imwrite() to direct the segmented images.
- We name the data frames and give its paths, for each species individually. We can consider improving the code by making a loop to automate the data frame containing all the data of every species.
- The code for the parametric map is functional but the results are not in line with the expectations, and it's difficult to understand what the different colors correspond to.
 




## CELLS CONNECTIONS

### How to use

0) Download the folder `cell_connections.zip`. 
You will find files `utils.py`, `xx`, `cell_connections.ipynb`, and a folder with images we worked on. 

1) Using your terminal, launch the Jupyter Notebook and open the Notebook `cell_connections.ipynb`.
2) Run the first block of the code in order to import all the imports needed, indicated in the jupyter notebook.


### Limitations 

- Sometimes, the algorithm identifies points that aren’t junctions because of the quality of the segmentation. We can either correct it manually or think about ways to improve the segmentation automatically. 


---------------------------------

## Database structure
Explanation on how our database is organized:

Vőfély, Róza V., Gallagher, Joseph, Pisano, Grace D., Bartlett, Madelaine, & Braybrook, Siobhan A. (2019). Data from: Of puzzles and pavements: a quantitative exploration of leaf epidermal cell shape [Data set]. https://doi.org/10.5061/dryad.g4q6pv3

### FDV_cell_database

This folder contains 116 .tif image files for stained epidermis sampled from various species. 
The species and sample names may be cross-referenced using the `global_database.csv` included in the `FDV_database` folder. 

Here is the format for naming the microscope images: 

- The first convention has a number of numeric fields separated by hyphens; fields 1 and 2 combined determine the species (see `global_database.csv` file); 
- Field 3 contains the magnification of the field; 
- Field 4 denotes the side of the leaf represented in the picture (i.e. adaxial or abaxial; please see `global_database.csv`); 
- Field 5 is an arbitrary numbering of the images from a leaf side.


When the orientation of the leaf is not set, it is unknown.

### FDV_leaf_database

- This folder contains 26 .png image files of photographs of various species. 
- The species and sample names may be cross-referenced using the `global_database.csv` included in the `FDV_database` folder. 


### global_database.csv

- This csv file contains the information about the 116 images from the database. 
- The first column `plant_name` contains the name of the species.
- The second column `cell_fname` contains the name of the file containing the microscopic image of the corresponding species. 



