from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?appid=030c795b56f90f24cdcbdfe9f908645a&units=metric&q="
    city = 'Delhi'

    if request.method== "POST":
        city = request.POST.get('cityname')

    r = requests.get(url+city).json();
    if len(r)==2:
        city_weather=''
    else:
        city_weather = {'city':city,'description':r['weather'][0]['description'],'icon':r['weather'][0]['icon'],'temperature':r['main']['temp']}

    return render(request,'weather_app/weather.html',context={'city_weather':city_weather})
