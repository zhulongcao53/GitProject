#!/usr/bin/python3
# encoding:utf-8
import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
	sitename = 'QxxRoBot'
	url = 'QxxRoBot.top'
	#新加一个列表
	list=[
		'主页',
		'星座运程',
		'和我聊天',
		'我的博客',
		'联系我吧',
	]
	context = {
		'sitename': sitename,
		'url':url,
		'list':list, #把list封装到context
	}
	#把上下文传递到模板里
	return render(request,'index.html',context)

@csrf_exempt
def QxRoBot(request):
    RobotResult = request.GET['RobotMessage']
    return render(request,'index.html',RobotResult)


def Reshtml(request):
    return render(request,'restest.html')
