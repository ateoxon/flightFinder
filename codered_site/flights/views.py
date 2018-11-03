from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse
# Create your views here.

class FlightByCountry(View):
	def get(self,request,fromc,to):
		return JsonResponse(request)

class FlightByProvinceState(View):
        def get(self,request,fromps,to):
                return JsonResponse(request)

class FlightByCity(View):
        def get(self,request,fromc,to):
                return JsonResponse(request)

class FlightByAirport(View):
        def get(self,request,froma,to):
                return JsonResponse(request)
