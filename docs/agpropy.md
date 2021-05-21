Here are some useful reference points for working with Python in ArcGIS Pro.

When you upgrade to a new version of ArcGIS Pro you will need to recreate your virtual environment.

`conda create --name propj arcgis python=3.7`

After creating the virt env, in the above it's called `propj`, then you can activate it.  

`conda activate propj`

Finally install the arcgis library which will install many dependencies.

`conda install -c esri arcpy arcgis`
