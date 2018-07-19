# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 11112))

print('Bind UDP on 11112...')

while True:
    data, addr = s.recvfrom(1024)
    print('Recieved from %s:%s' % addr)
    s.sendto(b'Hello, %s' % data, addr)

