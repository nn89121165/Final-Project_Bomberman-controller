import socket 
import json
import numpy as np
import matplotlib.pyplot as plot
HOST = '192.168.198.210'       # IP address 
PORT = 80            # Port to listen on (use ports > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        i=True
        while True:
            data= conn.recv(1024).decode('utf-8')
            print("Received from socket server:", data)
            if (data.count('{') != 1):
            # Incomplete data are received.
                continue
            obj = json.loads(data)
            t = obj['s']
            if i :#setting plot
                i= False
                plot.scatter(t, obj['x'], c='blue', label='x') # ax, ay, az
                plot.scatter(t, obj['y'], c='red',label='y')
                plot.scatter(t, obj['z'], c='green',label='z')
                plot.xlabel("sample num")
                plot.ylabel("Acceleration(cm/s^2)")
                plot.legend()
            plot.scatter(t, obj['x'], c='blue') # ax, ay, az
            plot.scatter(t, obj['y'], c='red')
            plot.scatter(t, obj['z'], c='green')
            plot.pause(0.001)