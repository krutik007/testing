from django.db import models

# Create your models here.
class Registration(models.Model):
	srollno=models.CharField(max_length=50,primary_key=True)
	sname=models.CharField(max_length=50)
	scity=models.CharField(max_length=50)

	def __str__(self):
		return self.sname+" "+self.scity

