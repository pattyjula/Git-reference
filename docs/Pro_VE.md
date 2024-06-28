Here are some useful reference points for working with Python in ArcGIS Pro.

# Creating virtual environment with ArcGIS Pro 
When you upgrade to a new version of ArcGIS Pro you will need to recreate your virtual environment. Below are the steps for upgrading in ArcGIS Pro 3.0.

Create a clone of the arcgis env

``conda create --clone arcgispro-py3 --name myenv``

or create a non Arc environment

`conda create --name myenv python=3.x`

After creating the virt env, activate it and install Arc library.

`conda install -c esri arcgis`

### Here are the steps to add files to be ignored by git

`cd .git`  

`nano .gitignore`  

Then add the file names to the .gitignore in a text editor  

### Python command from Git Bash command line

`alias python='winpty python.exe'`
