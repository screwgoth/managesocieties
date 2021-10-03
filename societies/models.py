from django.db import models

# Create your models here.
class Society(models.Model):
	society_name = models.CharField(max_length=100)
	address_1 = models.CharField(max_length=200)
	address_2 = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	zip_code = models.CharField(max_length=10)
	# society_photo = models.ImageField(upload_to='society_photos/')
	# members = models.ManyToManyField('auth.User', related_name='societies')

	def __str__(self):
		return self.name
