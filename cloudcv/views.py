from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageUploadForm
from .models import SourceImage
from . import image_processes

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
	pic_name = request.FILES['uploaded_image'].name
	pic_address = "/Users/WARL0CK/python/CloudCVToyTask/media/" + pic_name
	upload_form = ImageUploadForm(request.FILES)
	uploaded_image =  SourceImage(pic = request.FILES['uploaded_image'])
	uploaded_image.save()
	image_processes.make_grayscale(pic_name, pic_address)
	return render(request, "display.html")

