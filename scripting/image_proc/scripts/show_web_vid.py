import numpy as np
import cv2

# Open a sample video available in sample-videos
vcap = cv2.VideoCapture('https://www.sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4')
#vcap = cv2.VideoCapture('192.168.178.84:81/stream')
#if not vcap.isOpened():
#    print "File Cannot be Opened"

while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    #print cap.isOpened(), ret
    if frame is not None:
        # Display the resulting frame
        cv2.imshow('frame',frame)
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print ("Frame is None")
        break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print( "Video stop")