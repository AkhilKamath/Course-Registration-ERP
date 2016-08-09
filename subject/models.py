from django.db import models

# Create your models here.
class Degree(models.Model):
	code = models.CharField(max_length = 2)
	name = models.CharField(max_length = 50)

class Subject(models.Model):
	coursecode = models.CharField(max_length = 10)
	coursetitle = models.CharField(max_length = 100)
	credits = models.CharField(max_length = 10)
	compredate = models.CharField(max_length = 20)

	def __str__(self):
		return self.coursetitle

class SubjectOptions(models.Model):
	subject = models.ForeignKey(Subject, related_name = "options", on_delete = models.CASCADE)
	classcode = models.CharField(max_length = 10)
	section = models.CharField(max_length = 10)
	section = models.CharField(max_length = 10)
	instructors = models.CharField(max_length = 100)
	days = models.CharField(max_length = 30)
	room = models.CharField(max_length = 10)

class SemSubjects(models.Model):
	degree = models.ForeignKey(Degree, related_name = "semsubjects", on_delete = models.CASCADE)
	year = models.CharField(max_length = 1)
	sem = models.CharField(max_length = 1)
	subs = models.ManyToManyField(Subject)
