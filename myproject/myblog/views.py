#!/usr/bin/python3
# encoding:utf-8
import json
import requests
from myblog.models import Menulist, Blog, Photo, PhotoType, About
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    SiteName = 'QxxRoBot'
    Menu = Menulist.objects.all()
    Photos = Photo.objects.all()
    PhotoTypes = PhotoType.objects.all()
    AboutMe = About.objects.all()
    context = {
        'SiteName': SiteName,
        'Menulist': Menu,
        'Photo': Photos,
        'PhotoType': PhotoTypes,
        'AboutMe': AboutMe,
        
    }
    return render(request,'index.html', context)

