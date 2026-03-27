#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from config import *
from data_processing import *
from idw_interpolation import *
from plotting import *
import numpy as np

# Read shapefiles
xmin, ymin_shp, xmax_shp, ymax, boundary_shapes, ls_x, ls_y = read_shapefiles(boundary_fp, landslide_fp)

# Apply cropping
ymin = ymin
xmax = xmax

# NDVI processing
ndvi_mean = process_ndvi(ndvi_dir)

# Subset
ndvi_mean = subset_region(ndvi_mean, xmin, xmax, ymin, ymax)

# Grid to points
points, vals = grid_to_points(ndvi_mean)

# IDW_interpolation
xi, yi = create_grid(xmin, xmax, ymin, ymax)
interp_points = np.column_stack((xi.ravel(), yi.ravel()))

zi = idw(points, vals, interp_points).reshape(xi.shape)

# Plot
plot_ndvi(xi, yi, zi, boundary_shapes, ls_x, ls_y, xmin, xmax, ymin, ymax)

