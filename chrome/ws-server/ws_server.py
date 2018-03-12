#!/usr/bin/env python

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import uuid


home_content = open('index.html').read()
home_js = open('index.js').read()


class MyHomePage(tornado.web.RequestHandler):
    def get(self):
        self.write(home_content)


class MyHomeJS(tornado.web.RequestHandler):
    def get(self):
        self.write(home_js)

#
#  External application simulation
#
ws_conns = {}

command_page = open('command.html').read()
command_js = open('command.js').read()


class MyCommandPage(tornado.web.RequestHandler):
    def get(self):
        self.write(command_page)


class MyCommandJS(tornado.web.RequestHandler):
    def get(self):
        self.write(command_js)


class MyWebSocketServer(tornado.websocket.WebSocketHandler):
    def open(self):
        self.id = uuid.uuid4()
        ws_conns[self.id] = {'id': self.id, 'socket': self}
        print('New connection')

    def on_message(self, message):
        print('New message: %s' % message)

    def on_close(self):
        ws_conns.remove(self.id)
        print('Closed connection')

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/websocketserver', MyWebSocketServer),
    (r'/index.js', MyHomeJS),
    (r'/', MyHomePage),
    (r'/command.html', MyCommandPage),
    (r'/command.js', MyCommandJS),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8000)

    tornado.ioloop.IOLoop.instance().start()
