import json as js, spatial, numpy as np
from laspy.file import File

#start_time = time.time()
#print("--- %s seconds ---" % (time.time() - start_time))


def get_header(filename):
    filename = r"D:\Smieci\Wewnetrzny\2015_07_18_transect_point_cloud_UTM.las"
    inFile = File(filename, mode="r")
    header = spatial.las_header(inFile.header)
    head_obj = js.dumps(header)
    inFile.close()
    return head_obj


def get_points_by_geom(filename, poly):
    poly = {"rings": [
            [661105.753, 5953550.459],
            [661142.424, 5953541.093],
            [661129.406, 5953513.153],
            [661099.026, 5953525.168],
            [661105.753, 5953550.459]
    ], "spatialReference": {"wkid": 2197}}
    filename = r"D:\Smieci\Wewnetrzny\2015_07_18_transect_point_cloud_UTM.las"
    inFile = File(filename, mode="r")
    results = spatial.las_within(inFile, poly["rings"], ["x", "y", "z"])
    json = js.dumps(results)
    inFile.close()
    return json


def get_stats_by_geom(filename, poly):
    poly = {"rings": [
            [661105.753, 5953550.459],
            [661142.424, 5953541.093],
            [661129.406, 5953513.153],
            [661099.026, 5953525.168],
            [661105.753, 5953550.459]
    ], "spatialReference": {"wkid": 2197}}
    filename = r"D:\Smieci\Wewnetrzny\2015_07_18_transect_point_cloud_UTM.las"
    inFile = File(filename, mode="r")
    results = spatial.las_within(inFile, poly["rings"], ["z"])
    inFile.close()
    stats = spatial.las_statistics(results["points"])
    return stats


