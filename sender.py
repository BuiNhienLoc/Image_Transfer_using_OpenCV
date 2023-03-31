import socket
import time
import imagezmq
import cv2
 
sender = imagezmq.ImageSender(connect_to='tcp://10.11.6.67:5555')
 
rpi_name = socket.gethostname() # send RPi hostname with each image
cap = cv2.VideoCapture("traffic.mp4")

while True:  # send images as stream until Ctrl-C
    print("hello")
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    sender.send_image(rpi_name, frame)

    if (cv2.waitKey(30)==27):
            break