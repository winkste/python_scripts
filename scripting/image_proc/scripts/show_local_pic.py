import cv2

img = cv2.imread('../resource/icon_new.png', 1)
#img = cv2.imread('http://192.168.178.103:81/stream', -1)

cv2.imshow('Icon Display', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
