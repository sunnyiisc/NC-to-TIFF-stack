"""
Created on 04 Nov, 2022 at 14:22
    Title: main.py - Converting and Stacking the bands from NETCDF4 to TIFF
    Description:
        -   ...
@author: Supantha Sen, nrsc, ISRO
"""

# Importing Modules
import xarray as xr
import rioxarray as rio

# Importing Custom Modules
from browse_gui import *


nc_file_path = browse_file('Select the netcdf file to open (.nc)')
tiff_save_path = browse_folder('Select the folder where you want to save')

nc_file = xr.open_dataset(nc_file_path)

band_stack = xr.Dataset()
for band in nc_file.data_vars:
    print('Converting ' + band + ' ...')
    band_stack[band] = nc_file[band]
    band_stack[band] = band_stack[band].rio.set_spatial_dims(x_dim='longitude', y_dim='latitude')
band_stack.fillna(0.0)

print('Writing file ...')

tiff_save_path_name = tiff_save_path + '/' + nc_file_path.split('/')[-2] + ".tiff"
band_stack.rio.set_crs("epsg:4326", inplace=True)
band_stack.rio.to_raster(tiff_save_path_name)

print('File Written :', tiff_save_path_name)
