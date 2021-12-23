'''
Instructions for loading file to ArcGIS Online

This is a simple, useful, and best-practice example for 
use with Python 3.7 and ArcGIS Pro 2.9 and is 
provided without warranty of any kind.

For security and learning purposes some steps are comments only.
'''

import arcpy
import arcgis
from arcgis.gis import GIS
import os
import zipfile

arcpy.env.overwriteOutput = True

# create query layer

arcpy.management.MakeQueryLayer(db, "queryLayer", """SELECT OBJECTID, Shape, GDB_GEOMATTR_DATA, value 
FROM source.file""", "OBJECTID", "POINT", "4326", 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision', "DEFINE_SPATIAL_PROPERTIES", "DO_NOT_INCLUDE_M_VALUES", "DO_NOT_INCLUDE_Z_VALUES", "-119.326209362609 33.3970626359568 -117.090481647225 34.8267769260519")

# export layer
with arcpy.EnvManager(transferDomains="TRANSFER_DOMAINS"):
    arcpy.conversion.FeatureClassToShapefile("queryLayer", output_path)
    
# create zip file here
zipfilename = ""

# connect to AGOL
site_internal = GIS(site, un, pw)

# Use shapefile or service definition not feature service ID
shp = site_internal.content.get('')

# Call the update method to replace/overwrite it with the zip file from disk
shp.update({}, zipfilename)
# Update feature layer
shp.publish(overwrite=True)

print(':)')
