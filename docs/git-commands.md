Here are some useful reference points for working with Python in ArcGIS Pro.

# Creating virtual environment with ArcGIS Pro 
When you upgrade to a new version of ArcGIS Pro you will need to recreate your virtual environment. Below are the steps for upgrading to AGPro 3.0. The previous steps are kept below.

Create a clone of the arcgis env

``conda create --clone arcgispro-py3 --name myenv``

If the arcgis pro env is not found, run the command below for this non-standard conda install path and then try to create again.  
``conda config --add envs_dirs "C:\path to env folder you want to add\Python\envs"``  

Finally activate your virtual environment and ``import arcpy`` to confirm the library installed.

# Creating virtual environment within Git Bash (not for ArcGIS)

Run the below command to create a virt env.

`conda create --name myenv python=3.9`

After creating the virt env, then you can activate it.

`source activate myenv`

Finally conda or pip install additional libaries which will install dependencies. 

### Here are the steps to add files to be ignored by git

`cd .git`  

`nano .gitignore`  

Then add the file names to the .gitignore in a text editor  

