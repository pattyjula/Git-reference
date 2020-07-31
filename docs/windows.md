Set a proxy:  
`git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080`

Check the current proxy:  
`git config --global --get http.proxy`

Proxies can also be set through Environment Variables as a Variable and Value for a user.

Create a virtual environment  
`conda create -n testenv python=3.x anaconda`  

### GIS Stuff
Install <b>geopandas</b> on Windows 10  
1. Start virtual environment  
2. Enter the command below  
`conda install -c conda-forge geopandas`

Same for contextily for base map  
`conda install -c conda-forge/label/cf201901 contextily`

Matplotlib  
From within venv  
`pip install matplotlib`

Need to edit  
<i>Process to install geopandas on Windows Server 2019</i>  
Download the wheels for <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal">GDAL</a>, <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona">Fiona</a>, <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj">pyproj</a>, <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#rtree">rtree</a>, and <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely">shapely</a> from Gohlke  
Make sure you choose the wheel files that match your architecture (64-bit) and Python version (2.7 or 3.5). If Gohlke mentions any prerequisites in his descriptions of those 5 packages, install the prerequisites now (there might be a C++ redistributable or something similar listed there).
If OSGeo4W, GDAL, Fiona, pyproj, rtree, or shapely is already installed, uninstall it now. The GDAL wheel contains a complete GDAL installation – don’t use it alongside OSGeo4W or other distributions.  
Open a command prompt and change directories to the folder where you downloaded these 5 wheels.  
pip install the GDAL wheel file you downloaded. Your actual command will be something like: pip install GDAL-1.11.2-cp27-none-win_amd64.whl  
Add the new GDAL path to the windows PATH environment variable, something like C:\Anaconda\Lib\site-packages\osgeo  
pip install your Fiona wheel file, then your pyproj wheel file, then rtree, and then shapely.  
