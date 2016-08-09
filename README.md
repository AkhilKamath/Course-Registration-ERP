# Course-Registration-ERP

##Setup Instructions

1. Setup Python Virtual Environment (virtualenv): `virtualenv erp` .
2. Go into the Virtual Enviroment: `cd erp`
3. Activate the Environment: `source bin/activate`
4. Clone this repository: `git clone https://github.com/OSDLabs/Course-Registration-ERP erp`
5. Go into the cloned repository: `cd erp`
6. Install the dependencies: `pip install -r requirements.txt`
7. Run the webserver: `python manage.py runserver`
8. Webserver runs for default on `localhost:8000`. To set the port manually run `python manage.py runserver 8080` for `localhost:8080`

##Set Data for timetable

1. Navigate to the timetable folder. Make sure you have the timetable.xlsx. Run `python datamine.py`. This will port the data into JSON format in the data.json file. Now, go to `localhost:8000/setup`. This will migrate all the data into the SQLite database.

##Additional Instructions (For front-end developers)


##Login Credentials
1. Set superuser using `python manage.py createsuperuser`. Fill in the details. Open Admin Console from `localhost:8000/admin`

##Authors
Open Source Development Lab (BITS Goa)

##Issues
File issues in the issues section

##Contribution Guidelines

###For Front-end contributors (HTML, CSS, JS)
To edit the templates, go to the templates folder which has all the templates. Note that direct links \(\<a href\>\) won't work in Django backend. Hence please route it through the urls.py in erp folder.

###For Backend contributors (Python (Django))


##License
[License](https://github.com/OSDLabs/Course-Registration-ERP/blob/master/LICENSE.md)