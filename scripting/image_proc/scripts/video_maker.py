import cv2
import numpy as np
import glob

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
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter(img_folder + '/' +vid_name + '.mp4', fourcc, 15, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print('process completed...')


if __name__ == '__main__':
    print('video maker test:')
    #video_maker('/Volumes/Macintosh HD/Users/stephan_wink/workspace_github/python_scripts/scripting/image_proc/resource/2103241924', 'project')
    #video_maker('/Volumes/Macintosh HD/Users/stephan_wink/workspace_github/python_scripts/scripting/image_proc/resource/2104041603', 'project')
    video_maker('/Volumes/Macintosh HD/Users/stephan_wink/Downloads/2104162013', 'vid')