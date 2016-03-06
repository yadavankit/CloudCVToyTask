import cv2

def make_grayscale(pic_name, pic_address):
	im = cv2.imread(pic_address)
	gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	gray_name = "/Users/WARL0CK/python/CloudCVToyTask/media/gray_scale_" + pic_name
	cv2.imwrite(gray_name, gray)

def make_cannyedge():
	pass