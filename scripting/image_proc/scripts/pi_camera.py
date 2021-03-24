#https://cbrell.de/blog/opencv-mit-dem-raspberry-pi-ein-einstieg/

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy
import datetime
import os

image_counter = 10

img_avg = [0.0, 0.0, 0.0, 0.0, 0.0]

def check_brightness(image):
    global img_avg
    
    img_avg.append(numpy.average(image))
    del img_avg[0]
    #dark is an average < 10
    #standard light above the printer is 105
    #4max pro led is an average about 100
    if numpy.average(img_avg) > 15:
        return True
    else:
        return False

def check_timelapse_trigger(image):
    global image_counter

    if image_counter > 0:
        image_counter = image_counter - 1
        return True
    else:
        return False


def initialize_camera():
    print('initialize camera...')
    img_resolution = [320, 240]
    cam_framerate = 25
    cam_orientation = 90

    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (img_resolution[0], img_resolution[1])
    camera.framerate = cam_framerate
    camera.rotation = cam_orientation
    rawCapture = PiRGBArray(camera, size=(img_resolution[0], img_resolution[1]))

    print('warm up waiting...')
    # allow the camera to warmup
    time.sleep(1.5)
    return camera, rawCapture

def create_file_name():
    x = datetime.datetime.now()
    file_name = x.strftime('%y%m%d%H%M%S') + '_timelapse.mpeg4'
    return file_name

def create_folder_name():
    x = datetime.datetime.now()
    folder_name = x.strftime('%y%m%d%H%M')
    return folder_name


def main():
    timelapse_active = False
    file_name_path = None

    camera, rawCapture = initialize_camera()

    print('image capturing main loop...')
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize t$
        # and occupied/unoccupied text
        image = frame.array
        
        if False == timelapse_active:
            #check if the image is not dark
            timelapse_active = check_timelapse_trigger(image)
            timelapse_completed = False
            path = '/media/pi/UNTITLED/capture'
            #path = os.getcwd()
            #create folder for temporary jpeg images
            path = path + '/' + create_folder_name()
            try:
                os.mkdir(path)
            except OSError:
                print(f'Cteation of the directory {path} failed')
                timelapse_active = False
            else:
                print(f'created working directory {path}')
                x = datetime.datetime.now()
                file_name_path = x.strftime(path + '/' + '%y%m%d%H%M%S')
                image_index = 0
                cv2.imwrite(f'{file_name_path}_{image_index}.jpg', image)
                print(f'stored image: {file_name_path}_{image_index}.jpg')
                image_index = image_index + 1
        else:
            #check if the image is not dark
            timelapse_active = check_timelapse_trigger(image)
            if False == timelapse_active:
                timelapse_completed = True
            cv2.imwrite(f'{file_name_path}_{image_index}.jpg', image)
            print(f'stored image: {file_name_path}_{image_index}.jpg')
            image_index = image_index + 1
        
        if timelapse_completed == True:
            #store all images to a video and delete the images
            return
        
        time.sleep(1.0)

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)


        #if timecapsule is started, add image to video

        # show the frame
        #cv2.imshow("Frame", image)
        #key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        #if key == ord("q"):
        #    break



if __name__ == '__main__':
    #execute this script as standalone application
    main()