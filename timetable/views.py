from django.shortcuts import render
from django.conf import settings
import os
import json

# Create your views here.

def timetable(request):
	base_dir = settings.BASE_DIR
	with open(os.path.join("timetable","data.json")) as json_file:
		json_data = json.load(json_file)
	u.classcode = json_data[0]['classcode']
	context = {
		"u" : u,
	}
	return render(request, "timetable.html", context)