import cv2
import imagezmq

# create a ZMQ receiver object
receiver = imagezmq.ImageHub()

while True:
    # receive a frame from a remote device
    name, frame = receiver.recv_image()
    
    # display the frame
    cv2.imshow(name, frame)
    cv2.waitKey(1)

    # send a reply back to the sender
    receiver.send_reply(b'OK')
    
# close the window
cv2.destroyAllWindows()
