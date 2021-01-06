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

Use same kind of formatting for the text file as in the [lesson materials](https://automating-gis-processes.github.io/2016/Lesson3-geocoding.html#geocoding-in-geopandas), thus use semicolon `;` as a separator and add a unique integer number as `id` (doesn't matter what) for each center. 

- Geocode the addresses in Geopandas in a similar manner as was done in the [lesson materials](https://automating-gis-processes.github.io/2016/Lesson3-geocoding.html#geocoding-in-geopandas)

- Reproject the geometries into a EPSG projection 3879 similarly as in [lesson materials](https://automating-gis-processes.github.io/2016/Lesson3-projections.html#projections-converting-from-projection-to-another)
  
   - **Notice**: you need to pass the coordinate information as a proj 4 dictionary in a similar manner as in the lesson materials (see the second last bullet point in the [lesson materials](https://automating-gis-processes.github.io/2016/Lesson3-projections.html#projections-converting-from-projection-to-another)

- Make a Table join to retrieve the `id` column from original shopping centers DataFrame similarly as in [lesson materials](https://automating-gis-processes.github.io/2016/Lesson3-table-join.html)

- Save the GeoDataFrame as a Shapefile called `shopping_centers.shp`

## Task 2: Create buffers around shopping centers

Let's continue with our case study and calculate a 5 km `buffer` around the points. 

**Steps**

- Create a new column called `buffer` to your shopping-centers GeoDataFrame (or whatever you call it)

- Iterate over the rows in your GeoDataFrame and update the `buffer` column with a 5 km buffer Polygon.
  
  - Use Shapely's [buffer](http://toblerity.org/shapely/manual.html#object.buffer) function to create it (see the link for details how to use it)
  - You only need to use the `distance` -parameter, don't care about the other parameters.
  
- Replace the values in `geometry` column with the values of `buffer` column

## Task 3: How many people live within 5 km from shopping centers?

Last step in our analysis is to make a spatial join between our point-buffer layer and the same population grid that was [used in the lesson materials](https://automating-gis-processes.github.io/2016/Lesson3-spatial-join.html#download-and-clean-the-data).

**Steps**

- Read and prepare the population grid into a GeoDataFrame similarly as in [the lesson materials](https://automating-gis-processes.github.io/2016/Lesson3-spatial-join.html#download-and-clean-the-data)

- Make a spatial join between your buffered point layer and population grid layer

  - Note: Join the information now from buffer layer **into the population grid layer**

- Group the joined layer by shopping center index

- Calculate the sum of population living within 5 km for each shopping center.
  
  - Write the answers down here into the [Answers](#answers) section

## Answers

Write the amount of population living within 5km from each shopping center:

 - Itis:
 - Forum:
 - Iso-omena:
 - Sello:
 - Jumbo:
 - REDI:

## Hints

See hints for this exercise from [here](https://github.com/Automating-GIS-processes/Lesson-3-Geocoding-Spatial-Queries/blob/master/Lesson/Lesson-3-hints.md)

