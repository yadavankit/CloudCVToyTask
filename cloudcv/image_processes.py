import cv2
import numpy as np

def make_grayscale(pic_name, pic_address):
	im = cv2.imread(pic_address)
	gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	gray_name = "/Users/WARL0CK/python/CloudCVToyTask/media/gray_scale_" + pic_name
	cv2.imwrite(gray_name, gray)

def make_cannyedge(pic_name, pic_address):
	sigma = 0.3
	image = cv2.imread(pic_address)
	computed_median = np.median(image) 
	lower = int(max(0, (1.0 - sigma) * computed_median))
	upper = int(min(255, (1.0 + sigma) * computed_median))
	edged = cv2.Canny(image, lower, upper)
	canny_name = "/Users/WARL0CK/python/CloudCVToyTask/media/canny_" + pic_name
	cv2.imwrite(canny_name, edged)




