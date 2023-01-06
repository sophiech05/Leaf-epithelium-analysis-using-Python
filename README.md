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
pip install pandas

- Matplotlib
pip install matplotlib

- Napari
pip install napari

- Magicgui
pip install magicgui

- Skimage
pip install scikit-image

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
