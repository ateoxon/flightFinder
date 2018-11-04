from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse

from flights.cityCode import *
# Create your views here.

class FlightByCountry(View):
    def get(self,request,fromc,to):
        if fromc=="" or to=="":
            return JsonResponse({'success':False,'error':'empty arguments'})
        origin = getCode(str(fromc))
        destination = getCode(str(to))
        best, top5 = getFlights(origin, destination)
        dict = {"success":True,"best":best, "top5":top5}
        return JsonResponse(dict)

class FlightByProvinceState(View):
    def get(self,request,fromc,fromps,toc,to):
        if fromc == "" or fromps=="" or toc=="" or to=="":
            return JsonResponse({'success':False,'error':'no arguments'})
        from_loc = "{}-{}".format(fromps,fromc)
        to_loc = "{}-{}".format(to,toc)
        origin = getCodeDB(from_loc)
        destination = getCodeDB(to_loc)
        best, top5 = getFlights(origin,destination)
        return JsonResponse({'success':True,'best':best,'top5':top5})

class FlightByCity(View):
    def get(self,request,fromc,froms,fromci,to,tos,toci):
        if fromc=="" or froms=="" or fromci=="" or to=="" or tos=="" or toci=="":
            return JsonResponse({'success':False,'error':'empty arguments'})
        from_country_code = getCode(fromc)
        to_country_code = getCode(to)
        from_state_code = getStateCode(froms)
        to_state_code = getStateCode(tos)
        from_loc = "{}-{}".format(from_country_code,from_state_code)
        to_loc = "{}-{}".format(to_country_code,to_state_code)
        origin = getCodeDB(from_loc)
        destination = getCodeDB(to_loc)
        best, top5 = getFlights(origin,destination)
        return JsonResponse({'success':True,'best':best,'top5':top5})

def index(request):
    return render(request,'index.html')

def search(request,fromc,toc):
    return render(request,'index2.html')
