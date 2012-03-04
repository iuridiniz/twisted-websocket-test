import sys
import os
from twisted.python import log
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.web import static

from websocket import WebSocketSite, WebSocketHandler

class Echo(WebSocketHandler):
    def frameReceived(self, data):
        log.msg("Received data '%s'" % data.strip())
        self.transport.write(data)

def main(root_path=".", port=9091):
    ################
    # setup log
    log.startLogging(sys.stdout)
    ################
    # setup webserver
    webserver = None
    if root_path:
        # serve static files
        if not root_path.startswith("/"):
            root_path = os.path.join(os.path.dirname(__file__), root_path)
        root = static.File(root_path)
        webserver = WebSocketSite(root)
    else:
        # serve no files, only websockets
        webserver = WebSocketSite(resource.NoResource())

    ################
    # setup echo factory

    # add echo handler url
    webserver.addHandler("/ws/echo", Echo)

    ################
    # Run webserver
    reactor.listenTCP(port, webserver)
    reactor.run()

if __name__ == "__main__":
    main()
