#!/usr/bin/env python3

import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = '%d\n'%int(time.time())
        s.sendall(msg.encode('utf-8'))
        # data = s.recv(1024)
        time.sleep(1)


print('Received', repr(data))