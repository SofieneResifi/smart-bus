import socket
import threading
import time
__name__ = "__main__" 

HOST = '192.168.137.163'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def process_data_from_server(x):
    x1, y1 = x.split(",")
    return x1,y1


def my_client():
    threading.Timer(11, my_client).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        data = input("Enter command ")
        print('ggg')
        #my = "Data"

        my_inp = my.encode('utf-8')

        s.sendall(my_inp)

        data = s.recv(1024).decode('utf-8')

        x_temperature,y_humidity = process_data_from_server(data)

        print("Temperature {}".format(x_temperature))
        print("Humidity {}".format(y_humidity))

        s.close()
        time.sleep(5)


while 1:
    my_client()
