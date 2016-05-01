import cherrypy
from routes import Header, Points

if __name__ == '__main__':

    cherrypy.tree.mount(
        Header(), '/api/header',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.tree.mount(
        Points(), '/api/points',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()