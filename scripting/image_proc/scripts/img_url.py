import numpy as np
import urllib.request
import cv2

def url_to_image(url):
    with urllib.request.urlopen(url) as url:
        resp = url.read()
    image = np.asarray(bytearray(resp), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image


# initialize the list of image URLs to download
urls = [
	"http://192.168.178.84/capture",
    #"https://pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png",
	#"https://pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png",
]

# loop over the image URLs
for url in urls:
	# download the image URL and display it
	print("downloading %s" % (url))
	image = url_to_image(url)
	cv2.imshow("Image", image)
	cv2.waitKey(0)