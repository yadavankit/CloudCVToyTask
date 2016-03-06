from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageUploadForm
from .models import SourceImage
import cv2

################################################
# Index View
################################################

def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render())

################################################
# Display after uploading image
################################################

@csrf_exempt
def upload_image(request):
	upload_form = ImageUploadForm(request.FILES)
	uploaded_image =  SourceImage(pic = request.FILES['uploaded_image'])
	p.save()
	return render(request, "display.html")

