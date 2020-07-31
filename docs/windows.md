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
