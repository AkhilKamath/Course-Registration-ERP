from django.db import models

# Create your models here.

class timetable(models.Model):
	classcode = models.CharField(max_length = 10)
	coursecode = models.CharField(max_length = 10)
	coursetitle = models.CharField(max_length = 100)
	credits = models.CharField(max_length = 10)
	section = models.CharField(max_length = 10)
	stat = models.CharField(max_length = 10)
	instructors = models.CharField(max_length = 100)
	days = models.CharField(max_length = 30)
	room = models.CharField(max_length = 10)
	compredate = models.CharField(max_length = 20)

	def __str__(self):
		return self.coursetitle