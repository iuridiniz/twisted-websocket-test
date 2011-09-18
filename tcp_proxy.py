import sys
from twisted.python import log
from twisted.internet import reactor
from twisted.protocols.portforward import ProxyFactory
from websocket import WebSocketProtocol, WebSocketFactory

# When web browser connects on WebSocket it will redirect to this host/port
HOST, PORT = "localhost", 61613

def main():
    log.startLogging(sys.stdout)
    
    proxy_factory = ProxyFactory(HOST, PORT)
    ws_factory = WebSocketFactory(proxy_factory)

    #reactor.listenTCP(9090, proxy_factory)
    reactor.listenTCP(9091, ws_factory)

    reactor.run()

if __name__ == "__main__":
    main()
