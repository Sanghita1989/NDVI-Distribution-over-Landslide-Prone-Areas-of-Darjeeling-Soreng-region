#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

def plot_ndvi(xi, yi, zi, boundary_shapes, ls_x, ls_y, xmin, xmax, ymin, ymax):

    fig, ax = plt.subplots(figsize=(8, 6))

    levels = np.linspace(0, 1, 8)

    cf = ax.contourf(
        xi, yi, zi,
        levels=levels,
        cmap="viridis",
        vmin=0, vmax=1
    )

    for shp in boundary_shapes:
        x, y = zip(*shp.points)
        ax.plot(x, y, color="black", linewidth=1.4)

    ls_x_crop, ls_y_crop = [], []
    for x, y in zip(ls_x, ls_y):
        if (y >= ymin) and (x <= xmax):
            ls_x_crop.append(x)
            ls_y_crop.append(y)

    ax.scatter(ls_x_crop, ls_y_crop, color="black", s=15, label="Landslides")

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    cbar = plt.colorbar(cf, ax=ax, shrink=0.75)
    cbar.set_label("Mean NDVI")

    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("NDVI Distribution with Landslides")

    plt.legend()

    plt.savefig(
        r"D:\C drive_21-06-2025\Downloads\Downloads_18-02-2026\NDVI_landslide.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.tight_layout()
    plt.show()

