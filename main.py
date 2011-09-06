import sys
from twisted.python import log
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from websocket import WebSocketProtocol, WebSocketFactory

class Echo(Protocol):
    def dataReceived(self, data):
        log.msg("Received data '%s'" % data.strip())
        self.transport.write(data)


def main():
    echo_factory = Factory()
    echo_factory.protocol = Echo

    log.startLogging(sys.stdout)
    echo_ws_factory = WebSocketFactory(echo_factory)

    reactor.listenTCP(9091, echo_ws_factory)
    reactor.listenTCP(9090, echo_factory)
    reactor.run()


if __name__ == "__main__":
    main()
