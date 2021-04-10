#https://cbrell.de/blog/opencv-mit-dem-raspberry-pi-ein-einstieg/

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy
import datetime
import os
import glob


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


def initialize_camera():
    print('initialize camera...')
    img_resolution = [320, 240]
    cam_framerate = 25
    cam_orientation = 0

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

def video_maker(img_folder, vid_name):
    image_names = []
    img_array = []
    print('creating image file name list...')
    for filename in glob.glob(img_folder + '/*.jpg'):
        image_names.append(filename)
    image_names.sort()


    print('create image list...')
    for i in image_names:
        img = cv2.imread(i)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    print('write images to video file...')
    #fourcc = 0x00000021
    #fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    if len(img_array):
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        out = cv2.VideoWriter(img_folder + '/' +vid_name + '.mp4', fourcc, 15, size)
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
        print('process completed...')
        print('image stored: ' + img_folder + '/' +vid_name + '.mp4')
    else:
        print('no images found in: ' + img_folder)

def delete_tempo_pictures(img_folder):
    image_names = []

    print('prepare delete...')
    for filename in glob.glob(img_folder + '/*.jpg'):
        image_names.append(filename)
    print('delete files...')
    for i in image_names:
        os.remove(i)


def main():
    timelaps_state = 0
    file_name_path = None
    file_path = None

    camera, rawCapture = initialize_camera()

    print('image capturing main loop...')
    print('waiting for image capturing...')
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize t$
        # and occupied/unoccupied text
        image = frame.array

        printer_light_on = check_brightness(image)
        if 0 == timelaps_state:
            if printer_light_on:
                #start picture capturing
                path = '/media/pi/UNTITLED/capture'
                path = path + '/' + create_folder_name()
                try:
                    os.mkdir(path)
                except OSError:
                    print(f'Cteation of the directory {path} failed')
                else:
                    print(f'created working directory {path}')
                    x = datetime.datetime.now()
                    file_name_path = x.strftime(path + '/' + '%y%m%d%H%M%S')
                    image_index = 0
                    cv2.imwrite(f'{file_name_path}_{image_index:010d}.jpg', image)
                    print(f'stored image: {file_name_path}_{image_index:010d}.jpg')
                    image_index = image_index + 1
                    timelaps_state = 1
        elif 1 == timelaps_state:
            if printer_light_on:
                cv2.imwrite(f'{file_name_path}_{image_index:010d}.jpg', image)
                print(f'stored image: {file_name_path}_{image_index:010d}.jpg')
                image_index = image_index + 1
            else:
                timelaps_state = 2
        elif 2 == timelaps_state:
                #create video and delete all temporary pictures
                video_maker(path, 'video')
                delete_tempo_pictures(path)
                timelaps_state = 0
                print('waiting for image capturing...')
        
        time.sleep(5.0)    

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)



if __name__ == '__main__':
    #execute this script as standalone application
    main()