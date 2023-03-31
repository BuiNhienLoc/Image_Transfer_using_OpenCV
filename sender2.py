import cv2
import imagezmq

# create a ZMQ sender object
sender = imagezmq.ImageSender(connect_to='tcp://<ip_address>:5555')

# open the camera
cap = cv2.VideoCapture(0)

while True:
    # read a frame from the camera
    ret, frame = cap.read()
    
    # send the frame to the remote device
    sender.send_image('jetson_nano', frame)
    
    # display the frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the camera and close the window
cap.release()
cv2.destroyAllWindows()