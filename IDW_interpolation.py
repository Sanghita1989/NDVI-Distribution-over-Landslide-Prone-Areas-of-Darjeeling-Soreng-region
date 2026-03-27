#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from scipy.spatial import cKDTree

def idw(xy, values, xi, power=2):
    tree = cKDTree(xy)

    k = min(8, len(values))
    dist, idx = tree.query(xi, k=k)

    dist[dist == 0] = 1e-10

    weights = 1.0 / (dist ** power)
    return np.sum(weights * values[idx], axis=1) / np.sum(weights, axis=1)


def create_grid(xmin, xmax, ymin, ymax):
    xi, yi = np.meshgrid(
        np.linspace(xmin, xmax, 350),
        np.linspace(ymin, ymax, 350)
    )
    return xi, yi

