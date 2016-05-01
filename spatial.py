import numpy as np
import matplotlib.path as mpl_path


# Uwaga nie wspiera roznych ukladow odniesienia

def validate_geom(geometry):
    try:
        sr = geometry["spatialReference"]
        rings = geometry["rings"]
        return True
    except:
        return False


def las_within(points_file, polygon, parameters, point_export = False):
    bb_path = mpl_path.Path(np.array(polygon))
    coords = np.vstack((points_file.x, points_file.y)).transpose()
    point_tester = bb_path.contains_points(coords)
    params_list = []
    for param in parameters:
        params_list.append(getattr(points_file, param, None)[np.where(point_tester)])

    return_arr = np.vstack(tuple(params_list)).transpose()

    if point_export == True:
        return return_arr.tolist()
    else:
        return_obj = {"params": parameters, "points": return_arr.tolist()}
        return return_obj


def las_statistics(z_array):
    num_array = np.array(z_array)
    minVal = num_array.min()
    maxVal = num_array.max()
    meanVal = np.mean(num_array)
    std = np.std(num_array)
    return {"MIN": minVal, "MAX": maxVal, "MEAN": meanVal, "STD": std}


def las_header(hdr):
    return {
        "version": hdr.version,
        "filesource_id": hdr.filesource_id,
        #"reserved": 0,
        "guid": hdr.guid.urn, #TODO zweryfikowac do konca obiekt {UUID}
        "system_id": hdr.system_id,
        "software_id": hdr.software_id,
        "date": hdr.date.microsecond,
        "header_size": hdr.header_size,
        "data_offset": hdr.data_offset,
        "vlrs_count": len(hdr.vlrs),
        "dataformat_id": hdr.dataformat_id,
        "data_record_length": hdr.data_record_length,
        "number_points": hdr.count,
        "point_return_count": hdr.point_return_count,
        "scale": hdr.scale,
        "offset": hdr.offset,
        "min": hdr.min,
        "max": hdr.max}
