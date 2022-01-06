Here are some useful reference points for working with Python in ArcGIS Pro.

# Upgrading ArcGIS Pro
When you upgrade to a new version of ArcGIS Pro you will need to recreate your virtual environment.

`conda create --name pro python=3.7`

After creating the virt env, in the above it's called `pro`, then you can activate it.  

`conda activate pro`

Finally pip install the arcgis library which will install many dependencies.

`conda install arcpy=2.9 -c esri`

Downgrade environment for nbconvert

'conda install "nbconvert=5.6.1"'
