HTTPS - PY4E

Tcp - Transport Control Protocol

The transport laywer control the computer comunication.

TCP Connections / Sockets = an endpoint of a bidirectional inter-process comunication flow across an internet protocol-based.

Process(Browser) <- internet -> process(web)

Tcp Port Number = it's the apllication-specific software numbert to communication; it allows multiple networked applications to same server.

Sockets in python -

`import socket mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) mysock.connect(('data.pr4e.org', 80))

`
What we want to do with the socket?
Application Protocols - Mail, World Wide Web.

What we gonna send and receive - Application Protocol.
Http - Hypertext transfer Protocol

Protocolo set the rules that all parties follow so we can predict each others behavior.

example hhttp://(its the protocol)www.dr-chuck.com/(host)/pages.html(document)

https://www.py4e.com/lessons/network# - 2.47
