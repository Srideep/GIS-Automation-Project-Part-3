# Geocoding and spatial join

This week we will practice how to do geocoding and spatial joins in Geopandas. The overall aim this week is to make practical study to find out how many people live within 5 km (Euclidian) distance from big shopping centers in Helsinki Region. 





## Task 1: Geocode shopping centers

In the first task the aim is to find out the addresses of shopping centers and geocoding them as a single Shapefile called `shopping_centers.shp`.

**Steps**

- From the internet we find out the addresses for following shopping centers and write the addresses into a text file called `shopping_centers.txt`:

 - Itis
 - Forum
 - Iso-omena
 - Sello
 - Jumbo
 - REDI (i.e. use the metro station of Kalasatama)



- We made a Table join to retrieve the `id` column from original shopping centers DataFrame similarly as in [lesson materials](https://automating-gis-processes.github.io/2016/Lesson3-table-join.html)

- Saved the GeoDataFrame as a Shapefile called `shopping_centers.shp`

## Task 2: Create buffers around shopping centers

Let's continue with our case study and calculate a 5 km `buffer` around the points. 

**Steps**

- We created a new column called `buffer` to our shopping-centers GeoDataFrame

- Iterated over the rows in our GeoDataFrame and update the `buffer` column with a 5 km buffer Polygon.
  
  - Use Shapely's [buffer](http://toblerity.org/shapely/manual.html#object.buffer) function to create it 
  - We only needed to use the `distance` -parameter, don't care about the other parameters.
  
- Replaced the values in `geometry` column with the values of `buffer` column

## Task 3: How many people live within 5 km from shopping centers?

Last step in our analysis is to make a spatial join between our point-buffer layer and the same population grid that was [used in the lesson materials](https://automating-gis-processes.github.io/2016/Lesson3-spatial-join.html#download-and-clean-the-data).

**Steps**

- We made a spatial join between your buffered point layer and population grid layer

  - Note: Join the information now from buffer layer **into the population grid layer**

- Grouped the joined layer by shopping center index

- Calculate the sum of population living within 5 km for each shopping center.
  
  - Wrote the answers down here into the [Findings](#Findings) section

## Findings

The amount of population living within 5km from each shopping center:

 - Itis:
 - Forum:
 - Iso-omena:
 - Sello:
 - Jumbo:
 - REDI:

