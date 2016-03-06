from django.conf.urls import url
from . import views

urlpatterns = [

	################################################
	# Index URL
	################################################

    url(r'^$', views.index, name='index'),

	################################################
	# Display URL
	################################################
	
    url(r'^display$', views.upload_image, name='display'),

    ]