import json, cherrypy
import las_manager as lm

class Header:
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self, filename = None):
        if filename == None:
            cherrypy.response.status = 400
            return "Missing filename parameter"
        else:
            header = lm.get_header("aa")
            return header

class Points:
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self, filename = None):
        if filename == None:
            cherrypy.response.headers["Status"] = "400"
            return "Missing filename parameter"
        else:
            points = lm.get_points_by_geom("aa", "aa")
            return points