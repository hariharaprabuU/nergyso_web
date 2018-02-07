# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from master.config import GALLERY_CATEGORY
from master.models import AbstractDefault
from forms import GalleryFileForm
from django.conf import settings

def update_image(request, filename):
	image_path = settings.IMAGES_ROOT
	image_root=image_path+"gallery_"+filename
	return image_root
	
# Create your models here.
class Gallery(AbstractDefault):
	gallery_title = models.CharField(verbose_name = 'Title', max_length = 255,help_text="Ex:Office")
	gallery_image = models.FileField(verbose_name = 'Images',upload_to = update_image,help_text="Supports Only jpg/png/jpeg format.")
	# gallery_category = models.CharField(verbose_name = 'Gallery Category', choices=GALLERY_CATEGORY,max_length=50)
	
	def __str__(self):
		return self.gallery_title

	def gal_image(self):
		files = str(self.gallery_image).split(',')
		filer=''
		if count > 1:
			for x in files:
				filer = filer + '<img src="'+settings.SITE_URL+'%s" width="100px"/>' % str(x) + '&nbsp;'
			return filer
		else:
			return 'None'
	gal_image.allow_tags = True
	gal_image.short_description = 'Image'

	class Meta:
		verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        ordering = ['id']
