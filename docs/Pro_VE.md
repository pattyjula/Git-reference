Here are some useful reference points for working with Python in ArcGIS Pro.

# Create virtual environment with ArcGIS Pro 
When you upgrade to a new version of ArcGIS Pro you will need to recreate your virtual environment. 

First, optionally set the directory where you want your virtual environments to be found.
  
``conda config --add envs_dirs "C:\ve\"``  

Create a clone of the arcgis env

`conda create --clone arcgispro-py3 --name myenv` 


Or run the commands below, using the Python specific version for the Pro release.

`conda create --name myenv python=3.x` 

`conda install -c esri arcgis` 

`conda install -c esri arcpy` 

# Create a non Arc environment

`conda create --name myenv python=3.x`
