from django.shortcuts import render
from django.conf import settings
#from rest_framework import status
#from rest_framework.response import Response
import json
import requests
import random
import string
#import sys
from django.http import JsonResponse, HttpResponse

,def multimedia_recommendation(request, ip):

    try:
        while True:
			access_key="8ee0660bb6cffbcd881a02a8bc76d56e"
            response = requests.get('api.ipstack.com/'+ip+'?access_key='+access_key+'&output=json'
            data = response.json()
            break
        return JsonResponse({'ip': data['ip'],'Language': data['Language']})

    except:
        return JsonResponse({'status':'false','message':'UNDEFINED ERROR'}, status=404)