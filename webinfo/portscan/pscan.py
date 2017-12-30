#!/usr/bin/python
a = "Script criado por Joas Antonio"
print a
import socket,sys

for port in range(1,65535):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((sys.argv[1], port)) == 0:
		print "Porta",port,"Esta Aberta"
		s.close()
