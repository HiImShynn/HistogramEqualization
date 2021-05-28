import os, sys
import cv2
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt 

def Creat_Histogram(img):
	assert len(img.shape) == 2		#check grayscale image
	histogram = [0] * 256			#list of intensity frequencies, 256 zero values
	for row in range (img.shape[0]):
		for col in range (img.shape[1]):
			histogram[img[row, col]] += 1	#creating Histogram statistic H(i)
	return histogram

def visualize_histogram(histogram, output = "histogram.jpg"):
	hist_data = pd.DataFrame ({"intensity": list(range(256)), "frequency": histogram})
	sns_hist = sns.barplot (x = "intensity", y = "frequency", data = hist_data, color = "red")
	sns_hist.set(xticks = [])

	fig = sns_hist.get_figure()
	fig.savefig(output)
	return output

def equalize_histogram(img, histogram):
	new_Z = [0] * 257						#Creat new Histogram statistics Z(i)
	for i in range(0, len(new_Z)):
		new_Z[i] = sum(histogram[:i])		#applying transforming algorithm Z(i) = Sum(H(j)) [j -> i]
	new_Z = new_Z[1:]

	max_value = max(new_Z)
	min_value = min(new_Z)					#scaling Z(i) to [0, 255]
	new_Z = [int(((f - min_value)/(max_value - min_value))* 255) for f in new_Z]		
	print ("H': ", new_Z)

	for row in range(img.shape[0]):			#applying Z(i) to image
		for col in range(img.shape[1]):
			img[row, col] = new_Z[img[row, col]]
	return img

def graph_plot(histogram):
	plt.clf()
	plt.plot(histogram, color = "red", linewidth = 2)
	plt.ylabel("frequency")
	plt.xlabel("intensity")
	plt.show()
	cv2.waitKey(0)

if __name__ == "__main__":
	assert len(sys.argv) ==2, '[USAGE] $ python %s lowcontrast2.jpg' % (os.path.basename(__file__), INPUT)
	INPUT = sys.argv[1]
	assert os.path.isfile(INPUT), '%s not found' %INPUT

	#read color images with grayscale flag: "cv2.IMREAD_GRAYSCALE"
	img = cv2.imread(INPUT, cv2.IMREAD_GRAYSCALE)
	cv2.imshow("Orignal",img)		#showing original image
	
	#creat Histogram from Image
	histogram = Creat_Histogram(img)
	print("Histogram: ", histogram)
	graph_plot(histogram)

	#Equalizing Histogram of input image
	equalized_img = equalize_histogram(img, histogram)
	cv2.imwrite("equalized_%s" %INPUT, equalized_img)
	cv2.imshow("Equalized",equalized_img) #showing Equalized image
	print("Saved equalized image @equalized_%s" %INPUT)

	#Comparison between original Histogram and Equalized_Histogram
	new_histogram = Creat_Histogram(equalized_img)
	print("new_histogram: ", new_histogram)
	graph_plot(new_histogram)

	print("Done")