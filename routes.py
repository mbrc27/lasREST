import json, cherrypy
import las_manager as lm
import spatial as sp

class Header:
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self, filename = None):
        if filename == None:
            cherrypy.response.status = 400
            return "Missing filename parameter"
        else:
            filename = str(filename)
            header = lm.get_header(filename)
            return header


class Points:
    exposed = True
    @cherrypy.tools.accept(media='text/plain')
    def GET(self, filename = None, geometry = None):
        if filename == None or geometry == None:
            cherrypy.response.headers["Status"] = "400"
            return "Missing parameters"
        else:
            filename = str(filename)
            geometry = json.loads(geometry)
            if sp.validate_geom(geometry):
                points = lm.get_points_by_geom(filename, geometry)
            else:
                return "Wrong geometry"

            return points

    @cherrypy.tools.accept(media='text/plain')
    def POST(self, filenames = None, geometry = None):
        if filenames == None or geometry == None:
            cherrypy.response.headers["Status"] = "400"
            return "Missing parameters"
        else:
            filenames = json.loads(filenames)
            geometry = json.loads(geometr)
            if isinstance(filenames, list):
                if sp.validate_geom(geometry):
                    points = lm.get_points_by_geom_mfn(fn, geometry)
                    return points
                else:
                    return "Wrong geometry"
            else:
                return "Wrong filenames parameter type"


class Statistics:
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self, filename = None):
        return filename

    @cherrypy.tools.accept(media='text/plain')
    def POST(self, filenames = None):
        return filenames
