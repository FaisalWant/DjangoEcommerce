from django.db import models
import random 
import os

def get_filename_ext(filpath):
	base_name=os.path.basename(filepath)
	name, ext=os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	print(instance)
	print(filename)
	new_filename=random.randint(1,39)
	name, ext= get_filename_ext(filename)
	final_filename= '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(
		new_filename=new_filename,
		final_filename=final_filename
		)
# Create your models here.
class Product(models.Model):  
	title = models.CharField(max_length=123)
	description=models.TextField()
	price= models.DecimalField(decimal_places=2, max_digits=10, default=39.9)
	image= models.ImageField(upload_to='products/',null= True, blank=True)
	def __str__(self):
		return self.title
		