from django import forms

################################################
# Image Upload Form
################################################

class ImageUploadForm(forms.Form):
	image = forms.ImageField()