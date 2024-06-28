Here are some useful reference points for working with Python in ArcGIS Pro.

# Creating virtual environment with ArcGIS Pro 
When you upgrade to a new version of ArcGIS Pro you will need to recreate your virtual environment. Below are the steps for upgrading in ArcGIS Pro 3.0.

Create a clone of the arcgis env

``conda create --clone arcgispro-py3 --name myenv``

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

### Python command from Git Bash command line

`alias python='winpty python.exe'`
