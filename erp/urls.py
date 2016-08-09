"""erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from timetable import views as timetableviews
from home import views as homeviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^timetable/$', timetableviews.timetable, name = 'timetable'),
    url(r'^setup/$', timetableviews.setup, name = 'setup'),
    url(r'^login/$', homeviews.login_view, name = 'login'),
    url(r'^dashboard/$', homeviews.Dashboard, name = 'dashboard'),
    url(r'^$', homeviews.home)
]
