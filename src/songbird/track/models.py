from django.db import models
from django.conf import settings 



# Create your models here.
class Track (models.Model):
	author 			 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	track_name		 =  models.CharField(max_length = 300)
	track_file 		 =  models.FileField()
	genre 			 =  models.CharField(max_length = 350)
	tags			 =  models.CharField(max_length = 3000)

	created_at		 = models.DateTimeField(auto_now_add = True)


	def __str__(self):
		return self.track_name



