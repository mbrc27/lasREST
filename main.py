import cherrypy, os
from routes import Header, Points

cherrypy.config.update({'server.socket_port': 3000})

class MapApp(object):
    @cherrypy.expose
    def index(self):
        return "aaabbb" #open('index.html')


if __name__ == '__main__':
     webapp = MapApp()

     app_conf = {
         '/': {
             'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './public'
         }
     }

     cherrypy.tree.mount(MapApp(), '/', app_conf)

     cherrypy.tree.mount(Header(), '/api/header', {
         '/': {
             'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
             'tools.response_headers.on': True,
             'tools.response_headers.headers': [('Content-Type', 'text/plain')],
         }
     })
     cherrypy.tree.mount(Points(), '/api/points', {
         '/': {
             'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
             'tools.response_headers.on': True,
             'tools.response_headers.headers': [('Content-Type', 'text/plain')],
         }
     })
     cherrypy.tree.mount(Header(), '/api/stats', {
         '/': {
             'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
             'tools.response_headers.on': True,
             'tools.response_headers.headers': [('Content-Type', 'text/plain')],
         }
     })

     cherrypy.engine.start()
     cherrypy.engine.block()





