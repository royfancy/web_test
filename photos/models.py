from django.db import models

# Create your models here.


from django.utils import timezone

class Photo (models.Model):
	#兩個欄位                 (指定資料夾:upload_to='image/')
	image = models.ImageField(upload_to='image/',blank=False,null=False)
	upload_date = models.DateField(default=timezone.now)