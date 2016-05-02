import json as js, spatial, os, numpy as np
from laspy.file import File

#start_time = time.time()
#print("--- %s seconds ---" % (time.time() - start_time))


def get_header(filename):
    inFile = File(filename, mode="r")
    header = spatial.las_header(inFile.header)
    head_obj = js.dumps(header)
    inFile.close()
    return head_obj


def get_points_by_geom(filename, poly):
    inFile = File(filename, mode="r")
    results = spatial.las_within(inFile, poly["rings"], ["x", "y", "z"])
    json = js.dumps(results)
    inFile.close()
    return json


def get_points_by_geom_mfn(filenames, poly):
    points = []
    for fn in filenames:
        inFile = File(fn, mode="r")
        results = spatial.las_within(inFile, poly["rings"], ["x", "y", "z"], True)
        points += results
    return js.dumps({"params": ["x", "y", "z"], "points": points})


def get_stats_by_geom(filename, poly):
    inFile = File(filename, mode="r")
    results = spatial.las_within(inFile, poly["rings"], ["z"])
    inFile.close()
    stats = spatial.las_statistics(results["points"])
    json = js.dumps(stats)
    return json


def get_stats_by_geom_mfn(filenames, poly):
    points = []
    for fn in filenames:
        inFile = File(fn, mode="r")
        results = spatial.get_stats_by_geom(inFile, poly["rings"], ["z"], True)
        points += results
    return js.dumps({"params": ["z"], "points": points})
