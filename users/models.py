from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):

	city = [('riyadh', 'Riyadh Province -  الرياض'),('jeddah', 'Jeddah Province -  جدة'),
     ('medinah', 'Medinah Province -  المدينة'), ('makkah', 'Makkah Province - مكة'), ('qassim', 'Qassim Province - القصيم'),
      ('easter', 'Easter Province - المنطقه الشرقيه'), ('asir', 'Asir Province -  عسير'), ('tabuk', 'Tabuk Province -  تبوك'),
       ('hail', 'Hail Province -  حايل'), ('northern', 'Norther Borders -  منطقة الحدود الشماليه'), ('jizan', 'Jizan Province -  جيزان'),
        ('tabuk', 'Tabuk Province -  تبوك'), ('bahah', 'Bahah Province -  الباحة'), ('najran', 'Najran Province -  نجران')]

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics ')
	city = models.CharField(max_length=20, choices=city,default='riyadh',null=True)
	phone = models.CharField(max_length=10,null=True)
	first_name = models.CharField(max_length=20,null=True)
	last_name = models.CharField(max_length=20,null=True)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self,*args,**kawrgs):
		super().save(*args,**kawrgs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)




