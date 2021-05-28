import cv2
import os, sys
import numpy as np
from matplotlib import pyplot as plt

def Color_Image_Histogram(img):
	img_bgr = cv2.imread(img)
	ycrcb_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)
	color = ("b", [0, 0, 0, 0], [0, 0, 0, 0])

	plt.figure()
	for i, col in enumerate(color):
		histr = cv2.calcHist([ycrcb_img], [i], None, [256], [0, 256])
		plt.plot(histr, color = col)
	plt.xlim([0, 256])
	plt.xlabel("frequency")
	plt.ylabel("intensity")
	plt.show()
	cv2.waitKey()

def Color_Image_Equalizing(img):
	rgb_img = cv2.imread(img)
	cv2.imshow("Original Image", rgb_img)
	ycrcb_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2YCrCb)
	ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])
	cv2.imshow("equalized_YCrCb_image", ycrcb_img)
	
	equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)
	cv2.imshow("equalized_img", equalized_img)


	color = ("b", [0, 0, 0, 0], [0, 0, 0, 0])

	plt.figure()
	for i, col in enumerate(color):
		histr = cv2.calcHist([ycrcb_img], [i], None, [256], [0, 256])
		plt.plot(histr, color = col)
	plt.xlim([0, 256])
	plt.xlabel("frequency")
	plt.ylabel("intensity")
	plt.show()
	cv2.waitKey()

	return equalized_img

assert len(sys.argv) == 2, "[USAGE] $ python %s lowcontrastcolor.jpg" % (os.path.basename(__file__), INPUT)
INPUT = sys.argv[1]
assert os.path.isfile(INPUT), "% not found" %INPUT

cv2.imshow("Original Image", cv2.imread(INPUT))

Color_Image_Histogram(INPUT)
Color_Image_Equalizing(INPUT)
print("Done")
# equalized_histogram = Color_Image_Equalizing(INPUT)
# Color_Image_Equalizing(equalized_histogram)
