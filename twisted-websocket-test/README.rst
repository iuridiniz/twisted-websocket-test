============================
Test WebSocket using twisted
============================

This project tests a WebSocket server implementation using twisted

Keywords:

* Javascript
* WebSocket
* Python
* Twisted
* Stomp

**Requirements:**

* python
* twisted
* stomp message broker (optional)

echo.py
-------

Example of an echo service 

How to run::
  
    $ python ./echo.py

How to use

    Open echo.html file on any websocket capable browser (Chrome, Safari, ...)
  
    Windows::
    
        > start echo.html
  
    Linux::
    
        $ xdg-open echo.html


tcp_proxy.py
--------------

This example just exposes an existing service over WebSocket. 
*It's necessary to use some implentation of the service protocol over 
WebSocket*

In this example, it will redirect WebSocket connections to a stomp message 
broker running on localhost:61613 over WebSocket, but may be any service.

Stomp protocol implementation over WebSocket used in this example is 
available at https://github.com/jmesnil/stomp-websocket. See more information
about it at http://jmesnil.net/stomp-websocket/doc/

How to run::
  
    $ python ./tcp_proxy.py

How to use:
  
    *Make sure that stomp message broker is running on localhost:61613*
   
    Open stomp.html on any websocket capable browser (Chrome, Safari, ...)

    Windows::
    
        > start echo.html
  
    Linux::
    
        $ xdg-open ./echo.html


websocket.py
------------
Blind (re)implementation of WebSockets as a standalone wrapper for Twisted
protocols.
Got from: http://paste.pocoo.org/show/451569/
