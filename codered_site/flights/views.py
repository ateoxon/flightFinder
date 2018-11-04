from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse

from . import cityCode
# Create your views here.

class FlightByCountry(View):
    def get(self,request,fromc,to):
            origin = getCode(str(fromc))
            destination = getCode(str(to))
            best, top5 = getFlights(origin, destination)
            dict = {"best":best, "top5":top5}

            return JsonResponse(dict.json())

class FlightByProvinceState(View):
        def get(self,request,fromps,to):
            origin = getCode(str(fromc))
            destination = getCode(str(to))
            best, top5 = getFlights(origin, destination)
            dict = {"best":best, "top5":top5}

            return JsonResponse(dict.json())

class FlightByCity(View):
        def get(self,request,fromc,to):
            origin = getCode(str(fromc))
            destination = getCode(str(to))
            best, top5 = getFlights(origin, destination)
            dict = {"best":best, "top5":top5}

            return JsonResponse(dict.json())

class FlightByAirport(View):
        def get(self,request,froma,to):
            origin = getCode(str(fromc))
            destination = getCode(str(to))
            best, top5 = getFlights(origin, destination)
            dict = {"best":best, "top5":top5}

            return JsonResponse(dict.json())

def index(request):
    return render(request,'index2.html')

