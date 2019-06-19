from django.db import models

# Create your models here.
class Product(models.Model):  
	title = models.CharField(max_length=123)
	description=models.TextField()
	price= models.DecimalField(decimal_places=2, max_digits=10, default=39.9)


 