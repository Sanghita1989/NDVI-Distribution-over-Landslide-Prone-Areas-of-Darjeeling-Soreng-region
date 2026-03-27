## NDVI-landslide-analysis/-Workflow
│── config.py
│── data_processing.py
│── idw_interpolation.py
│── plotting.py
│── main.py

## Study Area
Darjeeling–Soreng region (Eastern Himalayas), a landslide-prone mountainous terrain where vegetation plays a crucial role in slope stability.

## Objectives

This project investigates the impact of long-term vegetation cover (NDVI) on landslide events using satellite-derived NDVI data and observed landslide locations. The region is categorized into different classes, from low to high vegetation, using the Inverse Distance Weighting (IDW) interpolation method.

## Methods
## 1. Data Processing

-Processing NDVI satellite data (.nc4 files)
-NDVI scaling 
-Mean NDVI calculated

## 2. Spatial Subsetting

-Study region extracted using shapefile boundary
-Additional constraints: Latitude ≥ 26.95 and Longitude ≤ 88.35

## 3. IDW Interpolation

-NDVI values are interpolated over a continuous grid using the Inverse Distance Weighting (IDW) method.

## 4. Landslide Overlay

Landslide locations are overlaid over the NDVI surface to analyze spatial correspondence between vegetation cover and landslide occurrence.

## 5. Vegetation Class Representation

NDVI values (0 to 1 range) are categorized into different classes representing:

-Low vegetation (sparse/bare surface) higher landslide susceptibility
-Moderate vegetation
-High vegetation (dense cover) improved slope stability

## Outputs-NDVI-landslide map

Interpolated NDVI surface (0–1 scale)
Landslide points overlay
Study boundary visualization
