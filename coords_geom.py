from shapely.geometry import Point, LineString, Polygon
import numpy as np

def createPointGeom(x_cord, y_cord):
    return Point(x_cord, y_cord)


def createLineGeom(lst_points): 
    line = []
    
    for elem in lst_points:
        if (isinstance(elem, Point)):
            line.append(elem)
            
    return LineString(line)


def createPolyGeom(lst_points):
    line = []
    
    for elem in lst_points:
        if (isinstance(elem, Point) or isinstance(elem, tuple)):
            line.append(elem)
            
    return Polygon(line)


def getCentroid(geometry):
    if (isinstance(geometry, Point) or isinstance(geometry, LineString) or isinstance(geometry, Polygon)):
        cen = geometry.centroid
        return cen


def getArea(geometry):
    if (isinstance(geometry, Polygon)):
        ar = geometry.area
        return ar


def getLength(geometry):
    if (isinstance(geometry, Polygon)or isinstance(geometry, LineString)):
        return geometry.length
    else:
        msg = "Error: LineString or Polygon geometries required!"
        return msg
    

def linestrings(orig_pts, dest_pts):
    lines = []
    for x,y in zip(orig_pts, dest_pts):
        lines.append(createLineGeom([x,y]))
    
    return lines

def euclidian_dist(orig_pts, dest_pts):
    linestring = linestrings(orig_pts, dest_pts)
    coords = [elem.xy for elem in linestring]
    x_coord = np.array([i[0] for i in coords])
    y_coord = np.array([j[1] for j in coords])
    
    sum_sq = np.sum(np.square(x_coord - y_coord))
    dist = np.sqrt(sum_sq)
    
    return dist

def helsinki_avg():
    travel_data = 'travelTimes_2015_Helsinki.txt'
    helsinki_data = np.loadtxt(travel_data, delimiter=';', usecols = (5,6,7,8,9,10), skiprows = 1)

    orig_points = []
    dest_points = []

    for elem in helsinki_data:
        from_x = elem[0]
        from_y = elem[1]
        to_x = elem[2]
        to_y = elem[3]
        orig_points.append(createPointGeom(from_x, from_y))
        dest_points.append(createPointGeom(to_x, to_y))

    euclidian_distance = euclidian_dist(orig_points, dest_points)
    print("The average distance of all Origin Destinations in the Helsinki area: {}".format(int(euclidian_distance)))

if __name__=='__main__':
   helsinki_avg()