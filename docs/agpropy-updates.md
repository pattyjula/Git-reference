Here are some useful reference points for working with Python in ArcGIS Pro.

# Upgrading ArcGIS Pro
When you upgrade to a new version of ArcGIS Pro you will need to recreate your virtual environment. Below are the steps for upgrading to AGPro 3.0. The previous steps are kept below.

Create a clone of the arcgis env

``conda create --clone arcgispro-py3 --name myenv``

If the arcgis pro env is not found, run the command below for this non-standard conda install path and then try to create again.  
``conda config --add envs_dirs "C:\path to env folder you want to add\Python\envs"``  

Finally activate your virtual environment and ``import arcpy`` to confirm the library installed.
