#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shapefile
import xarray as xr
import numpy as np

def read_shapefiles(boundary_fp, landslide_fp):
    boundary_shp = shapefile.Reader(boundary_fp)
    xmin, ymin, xmax, ymax = boundary_shp.bbox

    boundary_shapes = boundary_shp.shapes()

    ls_shp = shapefile.Reader(landslide_fp)
    ls_x, ls_y = [], []
    for s in ls_shp.shapes():
        x, y = s.points[0]
        ls_x.append(x)
        ls_y.append(y)

    return xmin, ymin, xmax, ymax, boundary_shapes, ls_x, ls_y


def process_ndvi(ndvi_dir):
    count = 0
    ndvi_sum = None

    for f in sorted(os.listdir(ndvi_dir)):
        if f.endswith(".nc4"):
            print("Processing:", f)

            ds = xr.open_dataset(os.path.join(ndvi_dir, f))

            ndvi = ds["ndvi"] / 10000
            ndvi = ndvi.mean(dim="time")

            if ndvi_sum is None:
                ndvi_sum = ndvi
            else:
                ndvi_sum = ndvi_sum + ndvi

            count += 1
            ds.close()

    ndvi_mean = ndvi_sum / count

    print("All files processed successfully")

    return ndvi_mean


def subset_region(ndvi_mean, xmin, xmax, ymin, ymax):
    lat_vals = ndvi_mean["lat"].values

    if lat_vals[0] < lat_vals[-1]:
        ndvi_mean = ndvi_mean.sel(
            lat=slice(ymin, ymax),
            lon=slice(xmin, xmax)
        )
    else:
        ndvi_mean = ndvi_mean.sel(
            lat=slice(ymax, ymin),
            lon=slice(xmin, xmax)
        )

    return ndvi_mean


def grid_to_points(ndvi_mean):
    lon2d, lat2d = np.meshgrid(
        ndvi_mean["lon"].values,
        ndvi_mean["lat"].values
    )

    vals = ndvi_mean.values

    points = np.column_stack((lon2d.ravel(), lat2d.ravel()))
    vals = vals.ravel()

    mask = ~np.isnan(vals)
    points = points[mask]
    vals = vals[mask]

    print("Number of NDVI points:", len(vals))

    return points, vals

