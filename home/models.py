from django.db import models
from django.contrib.auth.models import User
from subject.models import Degree

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	idno = models.CharField(max_length = 1)
	gender = models.CharField(max_length = 1)
	place = models.CharField(max_length = 30)
	dob = models.DateField()

class Name(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	primary = models.CharField(max_length = 100)
	preferred = models.CharField(max_length = 100)

class Addresses(models.Model):
	user = models.ForeignKey(User, related_name = "address", on_delete = models.CASCADE)
	country = models.CharField(max_length = 30)
	address = models.TextField()
	city = models.CharField(max_length = 30)
	pin = models.CharField(max_length = 6)
	state = models.CharField(max_length = 30)

PREF_CHOICES = (
	(u'Y',u'Yes'),
	(u'N',u'No'),
	)

class Phone(models.Model):
	user = models.ForeignKey(User, related_name = "phone", on_delete = models.CASCADE)
	ptype = models.CharField(max_length = 30)
	number = models.CharField(max_length = 30)
	ext = models.CharField(max_length = 10)
	preferred = models.CharField(max_length = 1, choices = PREF_CHOICES)
	emergency = models.CharField(max_length = 1, choices = PREF_CHOICES)

class Email(models.Model):
	user = models.ForeignKey(User, related_name = "email", on_delete = models.CASCADE)
	mtype = models.CharField(max_length = 30)
	address = models.EmailField()
	preferred = models.CharField(max_length = 1, choices = PREF_CHOICES)

DEGREETYPE_CHOICES = (
	(u'Dual',u'Dual'),
	(u'Main',u'Main'),
	(u'Minor',u'Minor'),
	)

class Degree(models.Model):
	user = models.ForeignKey(User, related_name = "degree", on_delete = models.CASCADE)
	dtype = models.CharField(max_length = 10, choices = DEGREETYPE_CHOICES)
	degree = models.ForeignKey(Degree, related_name = "degree", on_delete = models.CASCADE)



