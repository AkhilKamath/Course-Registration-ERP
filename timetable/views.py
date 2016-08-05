from django.shortcuts import render, redirect
from django.conf import settings
import os
import json
from .models import timetable as tmodel

# Create your views here.

def timetable(request):
	u = tmodel.objects.all()
	context = {
		"u" : u,
	}
	return render(request, "timetable.html", context)

def setup(request):
	with open(os.path.join("timetable","data.json")) as json_file:
		json_data = json.load(json_file)
	u = json_data

	for i in u:
		u = tmodel(
			classcode = i['classcode'],
			coursecode = i['coursecode'],
			coursetitle = i['coursetitle'],
			credits = i['creditslpu'],
			section = i['section'],
			stat = i['stat'],
			instructors = i['instructors'],
			days = i['days'],
			room = i['room'],
			compredate = i['compredate'],
			)
		u.save()
		print(u)

	return redirect('timetable')