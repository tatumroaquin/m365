#!/bin/env python
import sys, socket, time

target = input('Target IP: ')
minPort = int(input('min port: ') or 1)
maxPort = int(input('max port: ') or 65535)

ip = socket.gethostbyname(target)

start = time.time()
try:
    for port in range(minPort, maxPort):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f'port {port} is open')
        s.close()
except KeyboardInterrupt:
    print('Ctrl+C is pressed stopping program')
    sys.exit()
except socket.gaierror:
    print('Host could not be resolved')
    sys.exit()
except socket.error:
    print('No response, connection failed')
    sys.exit()
finish = time.time()

print(f'ETA {finish-start} seconds')
