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

<h2>Geopandas alternative install</h2> 
<i>Process to install geopandas on Windows Server 2019</i>  
<h3> Taken from <a href="https://geoffboeing.com/2014/09/using-geopandas-windows/" target="_blank">Geoff Boeing</a></h3>  
1. Download the wheels for <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal" target="_blank">GDAL</a>, <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona" target="_blank">Fiona</a>, <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj" target="_blank">pyproj</a>, <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#rtree" target="_blank">rtree</a>, and <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely" target="_blank">shapely</a> from Gohlke<br> 
2. Make sure you choose the wheel files that match your architecture (64-bit) and Python version (2.7 or 3.5). If Gohlke mentions any prerequisites in his descriptions of those 5 packages, install the prerequisites now (there might be a C++ redistributable or something similar listed there).  <br>
3. If OSGeo4W, GDAL, Fiona, pyproj, rtree, or shapely is already installed, uninstall it now. The GDAL wheel contains a complete GDAL installation – don’t use it alongside OSGeo4W or other distributions.<br>
4. Open a command prompt and change directories to the folder where you downloaded these 5 wheels.<br>
5. `pip install` the GDAL wheel file you downloaded. Your actual command will be something like: pip install GDAL-1.11.2-cp27-none-win_amd64.whl<br>
6. Add the new GDAL path to the windows PATH environment variable, something like c:\users\administrator\anaconda3\envs\geo_env\lib\site-packages\osgeo<br>
 `pip install` your Fiona wheel file, then your pyproj wheel file, then rtree, and then shapely.<br>   
7. Now you can `pip install geopanda` from command prompt or git bash<br>
