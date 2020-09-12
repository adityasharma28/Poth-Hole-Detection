#!/usr/bin/python36

import cv2
import requests
import numpy as np
url="http://192.168.43.1:8080/shot.jpg"
geturl=requests.get(url)
photoweb=geturl.content
photobyte=bytearray(photoweb)
np.array(photobyte)
imageId=np.array(photobyte)
frame=cv2.imdecode(imageId, -1)
cv2.imwrite("C:\Users\Asus\Desktop\try.png", frame)
cv2.destroyAllWindows()
