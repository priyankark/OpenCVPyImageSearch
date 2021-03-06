# This program accesses and manipulates pixels in an image
#some notes: r,g,b ordering is in reverse alaways and co-ordinate system is (0,0) at top left corner
from __future__ import print_function
import argparse
import cv2
ap=argparse.ArgumentParser()
ap.add_argument("-i","-image",required=True,help="Path to the image")
args=vars(ap.parse_args())
print(args)
image=cv2.imread(args["i"])
cv2.imshow("Original",image)
(b,g,r) = image[0,0]
print("Pixel at (0,0) Red: {} Blue: {} Green: {} ".format(r,g,b))
image[0,0]=(0,0,255)
(b,g,r)=image[0,0]
print("Pixel at (0,0)- Red: {} Blue: {} Green:{}".format(r,g,b))
#Getting a slice of the image and changing the color
corner=image[0:100,0:100]
cv2.imshow("corner",corner)
image[0:100,0:100]=(0,255,0)
cv2.imshow("Updated",image)
cv2.waitKey(0)

