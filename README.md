# Leaf-epithelium-analysis-using-Python


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


- Pandas

- Matplotlib

- Napari

- Magicgui

- Skimage

- Numpy

- Tifffile

- Glob

- Seaborn


## HOW MANY CELLS?

### How to use
This code will allow you to count the number of cells present on your microscopic photograph and to determine their positions. 
Here is how to use this code: 

1) Create a folder you can call 'how_many_cells'. 
2) Download 'utils.py' and 'how_many_cells.ipynb', and put them in this folder. 
3) In the folder 'how_many_cells', create another folder and name it 'images'. Then upload images you want to analyze into it. 
You should obtain this:
<img width="542" alt="Capture d’écran 2023-01-06 à 10 56 14" src="https://user-images.githubusercontent.com/122089106/210977974-219d8837-36d3-4ef2-add1-2fec23869fe5.png">

4) Using your terminal, launch the Jupyter Notebook and open the Notebook how_many_cells.
5) Run the first block of the code. You will have to enter 2 times the path leading to your photos. You will have to enter the full path, depending on where you put your how_many_cells folder. The following is an example of what you should enter: 
/Users/chavignysophie/Desktop/Bioinfo_project/how_many_cells/images
<img width="729" alt="Capture d’écran 2023-01-05 à 21 10 23" src="https://user-images.githubusercontent.com/122089106/210978454-7037d522-0c66-491e-af8e-76af39b628ed.png">

6) If your path is correct, you will see the following output:
<img width="1203" alt="Capture d’écran 2023-01-06 à 10 56 31" src="https://user-images.githubusercontent.com/122089106/210978658-9bd5bb92-315c-4104-ab47-acb8b665d863.png">

7) Now, run the 2nd window of code to open the Napari Viewer. Your Napari Viewer should open.
<img width="525" alt="Capture d’écran 2023-01-06 à 10 56 35" src="https://user-images.githubusercontent.com/122089106/210978749-e4abc90b-69d8-4e08-8002-71ff906d8eca.png">

8) Finally run this block of code in order to obtain the necessary widgets in your Napari:
<img width="714" alt="Capture d’écran 2023-01-06 à 10 56 47" src="https://user-images.githubusercontent.com/122089106/210978954-aec06f4c-fab1-4d15-b247-362d86eb8938.png">
<img width="1440" alt="Capture d’écran 2023-01-06 à 10 53 11" src="https://user-images.githubusercontent.com/122089106/210978989-326a4395-3e06-4b96-ab3d-fc6175dc0ae3.png">

9) Using the first widget, choose the image you want to analyze and click run.
<img width="970" alt="Capture d’écran 2023-01-06 à 10 57 01" src="https://user-images.githubusercontent.com/122089106/210979094-8146d0ce-d0b1-4bbe-9790-eb578dd39c45.png">
<img width="1420" alt="Capture d’écran 2023-01-06 à 10 49 30" src="https://user-images.githubusercontent.com/122089106/210979606-8e00e5be-923f-4890-b1af-20cfd88a793e.png">


10) Using the second widget, click on run and create a mask for your image. This mask should cover and label in different colors the cells you want to count. If the mask seems strange and does not label the cells correctly, you can play around with different parameters of the widget. For example, if your image has many very small cells you want to count, set min size objects at 0. 
The mask should ideally look like this: 
<img width="1436" alt="Capture d’écran 2023-01-06 à 10 51 48" src="https://user-images.githubusercontent.com/122089106/210979727-7078b972-33cd-484f-9704-45ecafd6f888.png">


Tip: if there are some labels that do not represent cells and are not able to better it by varying parameters, you can delete them manually. Click on “fill” and chose label 0, then delete the label simply by clicking on it on the image: 

<img width="249" alt="Capture d’écran 2023-01-06 à 10 52 55" src="https://user-images.githubusercontent.com/122089106/210979920-edff4689-fcad-48fb-a9b5-60ffdfc66b19.png">


11) When your mask seems good, use the last widget in order to count the cells and find their positions (centroids) by clicking on the run button. Do not forget to choose the right path according to the image you are processing, otherwise the data won’t be stored correctly.
<img width="1440" alt="Capture d’écran 2023-01-06 à 10 52 01" src="https://user-images.githubusercontent.com/122089106/210979971-d2141e07-2581-4895-af01-e2818cc7c57f.png">


12) Repeat this with all the images you want to analyze.
13) When you are done, you can collect your results in the folder 'how_many_cells' you created in the beginning. 
ou will see one csv file that summarizes all your results (name of the image, number of cells counted, name of the csv file with the positions of the cells/their centroids) and csv files with the positions of the cells/their centroids for each processed image.
This will look like this:  
<img width="792" alt="Capture d’écran 2023-01-06 à 10 57 11" src="https://user-images.githubusercontent.com/122089106/210980393-c86f0c72-3236-4f6c-ba73-366d38238b6a.png">


## Limitations 

The segmentation of some images is still not perfect even after changing characteristics. We can correct the mask manually but this takes time.
In the 'global_cell_count.csv' file created automatically, the column with the file names is missing and we should add it manually, which is also time consuming and therefore has to be improved.
We can consider improve the code so it can create automatically an additional folder 'results_per_image' in which will be saved all the csv files with the positions of the cells (instead of them be stored just next to the 'global_cell_count.csv' file). This will make the interpretation of the results easier and clearer. 



