import sys
from twisted.python import log
from twisted.internet import reactor
from twisted.protocols.portforward import ProxyFactory
from websocket import WebSocketProtocol, WebSocketFactory


#class Client(ProxyClient):
#    pass
#
#class ClientFactory(ProxyClientFactory):
#    protocol = Client
#
#class Server(ProxyServer):
#    clientProtocolFactory = ClientFactory

def main():
    log.startLogging(sys.stdout)

    stomp_proxy_factory = ProxyFactory("localhost", 61613)
    stomp_ws_factory = WebSocketFactory(stomp_proxy_factory)

    reactor.listenTCP(9090, stomp_proxy_factory)
    reactor.listenTCP(9091, stomp_ws_factory)

    reactor.run()


if __name__ == "__main__":
    main()
