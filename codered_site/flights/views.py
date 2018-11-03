from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse
# Create your views here.

class FlightByCountry(View):
	def get(self,request,fromc,to):
		pass
