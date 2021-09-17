import cv2
import sys

path = sys.argv[1]

img = cv2.imread(path)
#cv2.imshow('image', img)
#cv2.waitKey(0)

flipVertical = cv2.flip(img, 0)
#cv2.imshow('flipped image', flipVertical)
#cv2.waitKey(0)

text = "LIOR"
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 10
color = (0, 0, 0)
thickness = 5
lineType = cv2.LINE_AA

textsize = cv2.getTextSize(text, font, fontScale, thickness)[0]
h, w, _ = flipVertical.shape
org = (int(w / 2 - textsize[0] / 2 ) , int(h / 2  + textsize[1] / 2 ))

img_with_text = cv2.putText(flipVertical, text, org, font, fontScale, color, thickness, lineType)
cv2.imshow('flipped image with text', img_with_text)
cv2.waitKey(0)