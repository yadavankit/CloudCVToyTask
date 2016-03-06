from django.db import models

################################################
# Image Upload Model
################################################

class SourceImage(models.Model):

	pic = models.ImageField(upload_to = 'media/')


