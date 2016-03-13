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

def make_avg_blur(pic_name, pic_address):
	image = cv2.imread(pic_address)
	blur = cv2.blur(image, (5,5))
	blur_name = "/Users/WARL0CK/python/CloudCVToyTask/media/blur_" + pic_name
	cv2.imwrite(blur_name, blur)

def make_threshold(pic_name, pic_address):
	image = cv2.imread(pic_address)
	ret, threshold = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
	threshold_name = "/Users/WARL0CK/python/CloudCVToyTask/media/threshold_" + pic_name
	cv2.imwrite(threshold_name, threshold)

def make_bilateral_filter(pic_name, pic_address):
	image = cv2.imread(pic_address)
	bilateral_filter = cv2.bilateralFilter(image,9,75,75)
	bilateral_name = "/Users/WARL0CK/python/CloudCVToyTask/media/bilateral_filter_" + pic_name
	cv2.imwrite(bilateral_name, bilateral_filter)
	




