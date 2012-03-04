import sys
import os
from twisted.python import log
from twisted.internet import reactor
from twisted.protocols.portforward import ProxyFactory
from twisted.web import static, resource

from websocket import WebSocketSite, WebSocketWrapperFactory

def main(root_path=None, port=9091, proxy_url="/proxy", 
         proxy_host="www.google.com", proxy_port=80):
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
    # setup tcp proxy for a service
    # When web browser connects on WebSocket it will redirect to 
    # proxy_host/proxy_port
    proxy = ProxyFactory(proxy_host, proxy_port)
    ws = WebSocketWrapperFactory(proxy)

    webserver.addHandler(proxy_url, ws.buildHandler)

    ################
    # Run webserver
    reactor.listenTCP(port, webserver)
    reactor.run()

if __name__ == "__main__":
    main()
