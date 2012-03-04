============================
Test WebSocket using twisted
============================

This project tests a WebSocket server implementation using twisted

Keywords:

* Javascript
* WebSocket
* Python
* Twisted

**Requirements:**

* python
* twisted

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
*It's necessary to use some implentation in JavaScript of the service protocol 
over WebSocket*

In this example, it will redirect WebSocket connections to www.google.com:80 over 
WebSocket, but may be any service.

How to run::
  
    $ python ./tcp_proxy.py

How to use:
  
    Open tcp_proxy.html on any websocket capable browser (Chrome, Safari, ...)

    Windows::
    
        > start tcp_proxy.html
  
    Linux::
    
        $ xdg-open ./tcp_proxy.html


websocket.py
------------
Got from: git://github.com/iuridiniz/txWebSocket.git
