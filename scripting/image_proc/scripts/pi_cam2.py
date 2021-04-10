#https://cbrell.de/blog/opencv-mit-dem-raspberry-pi-ein-einstieg/

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy 

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
var1 = 1024
var2 = 768
camera.resolution = (var1, var2)
camera.framerate = 25
#camera.rotation = 90
rawCapture = PiRGBArray(camera, size=(var1, var2))
 
# allow the camera to warmup
time.sleep(1.5)

img_avg = [0.0, 0.0, 0.0, 0.0, 0.0]

def check_brightness(image):
    global img_avg
    
    #print(numpy.mean(image))
    img_avg.append(numpy.average(image))
    del img_avg[0]
    avg = numpy.average(img_avg)
    print(avg)
    #avg with light on: 95-97
    #avg with printer on: 77q-78
    #avg with both on: 93-94
    if avg > 15:
        return True
    else:
        return False

 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize t$
    # and occupied/unoccupied text
    #test
    image = frame.array

    #avg_color_per_row = numpy.average(image, axis=0)
    #avg_color = numpy.average(avg_color_per_row, axis=0)
    #avg_all = numpy.average(avg_color)
    #avg_all = numpy.average(image)
    #print(avg_all)
    #print(check_brightness(image))
    check_brightness(image)

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break