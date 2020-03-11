Set a proxy:  
`git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080`

Check the current proxy:  
`git config --global --get http.proxy`

Proxies can also be set through Environment Variables as a Variable and Value for a user.

Create a virtual environment  
`conda create -n testenv python=3.x anaconda`  

Install geopandas on Windows 10  
1. Start virtual environment  
2. Open Jupyter Notebook  
3. In a cell type command below  
`conda install -c conda-forge geopandas`
