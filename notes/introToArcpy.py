# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:59:25 2019

@author: jfrey
"""

import arcpy

environments = arcpy.ListEnvironments()

for i in environments:
    print(i, arcpy.env[i])
    


arcpy.env.workspace = "D:\\OneDrive\\Documents\\School Work\\Clark\\Python"

arcpy.Buffer_analysis("bus_routes", "bus_buffer_100ft", 100, "FULL","ROUND", "ALL")

arcpy.Clip_analysis('bus_buffer_100ft',"city_boundary","bus_buffer_100ft_worc")