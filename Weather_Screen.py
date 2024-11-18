from tkinter import *
import tkinter as tk
import time
from threading import Timer

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background="DeepSkyBlue2")

basepath = "c:/Weather_Forecast_Crop_Suggestion/"
from PIL import Image , ImageTk





icon_lookup = {
    'clear-day': "assets/Clear_Day.png",  # clear sky day
    'wind': "assets/Wind_New.png",   #wind
    'cloudy': "assets/Cloud_New.png",  # cloudy day
    'partly-cloudy-day': "assets/Partly_Cloud.png",  # partly cloudy day
    'rain': "assets/Rain_New.png",  # rain day
    'snow': "assets/Snow_New.png",  # snow day
    'snow-thin': "assets/Snow_New.png",  # sleet day
    'fog': "assets/FOG_F.png",  # fog day
    'clear-night': "assets/Clear_Moon.png",  # clear sky night
    'partly-cloudy-night': "assets/Partly_Cloud_Night.png",  # scattered clouds night
    'thunderstorm': "assets/Strom_New.png",  # thunderstorm
    'tornado': "assests/Tornado_New.png",    # tornado
    'hail': "assests/Hail_New.png"  # hail
}


def SHOW():
    from datetime import datetime
    now = datetime.now().time() # time object
    print("now =", now)
    print("type(now) =", type(now))	
    t = time.localtime()
    current_time = time.strftime('%I:%M %p', t)
    print(current_time)
    print("Called")
    time_label = tk.Label(root,text = str(current_time),font=("Times New Roman",42),bg="DeepSkyBlue2",fg="white")
    time_label.place(x=1090,y=10)
    t = Timer(3.0, SHOW)
    t.start() # after 30 seconds, "hello, world" will be printed"""

SHOW()




from datetime import date
import calendar
my_date = date.today()
day = calendar.day_name[my_date.weekday()]  #'Wednes
print(day)


from datetime import datetime
TODAY = datetime.today().strftime("%d/%m/%Y")

date_label = tk.Label(root,text = str(TODAY),font=("Times New Roman",35),bg="DeepSkyBlue2",fg="white")
date_label.place(x=1100,y=70)


from geopy.geocoders import Nominatim
from datetime import datetime,timedelta , date
import sys, requests
import json
DARK_SKY_API_KEY = "2981c8ba16e53d981a8e78b3e2953ca1"
option_list = "exclude=currently,minutely,hourly,alerts&amp;units=si"

future_dates = []
import datetime
for i in range(1,8):
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=i)
    print (NextDay_Date.strftime('%m-%d-%Y'))
    future_dates.append(NextDay_Date.strftime('%m-%d-%Y'))    
date_str1 = future_dates[0]
date_str2 = future_dates[-1]
from datetime import datetime,timedelta , date
date_object1 = datetime.strptime(date_str1, '%m-%d-%Y').date()
date_object2 = datetime.strptime(date_str2, '%m-%d-%Y').date()





d_from_date = date_object1
d_to_date = date_object2

delta = d_to_date - d_from_date       # as timedelta
import requests
import json

location_req_url='http://api.ipstack.com/103.51.95.183?access_key=fcdaeccb61637a12fdf64626569efab0'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)
location2 = "%s, %s" % (location_obj['city'], location_obj['region_code'])
print(location2.split(',')[0])

location = location2.split(',')[0]



lat = location_obj['latitude']
lon = location_obj['longitude']
longitude = lon
latitude = lat


from datetime import date, timedelta

MAX_TEMP = []
MIN_TEMP = []
DAY_TYPE = []
for i in range(delta.days+1):
  new_date = (d_from_date + timedelta(days=i)).strftime('%Y-%m-%d')
  search_date = new_date+"T00:00:00"
  response = requests.get("https://api.darksky.net/forecast/2981c8ba16e53d981a8e78b3e2953ca1/"+str(latitude)+","+str(longitude)+","+str(search_date)+"?"+str(option_list))
  json_res = response.json()
  DAY_TYPE.append(json_res['daily']['data'][0]['icon'])
  
  print("\n"+(d_from_date + timedelta(days=i)).strftime('%Y-%m-%d %A'))
  unit_type = '°F' if json_res['flags']['units'] == 'us' else '°C'
  #print("Min temperature: "+str(json_res['daily']['data'][0]['apparentTemperatureMin'])+unit_type)
  #print(json_res)
  temp = (json_res['daily']['data'][0]['apparentTemperatureMin']-32) * 5/9
  MIN_TEMP.append(str(temp)[:2])
  print("Min temperature in *C: "+str(temp))
  #print("Max temperature: "+str(json_res['daily']['data'][0]['apparentTemperatureMax'])+unit_type)
  temp = (json_res['daily']['data'][0]['apparentTemperatureMax']-32) * 5/9
  MAX_TEMP.append(str(temp)[:2])
  print("Max temperature in *C: "+str(temp))
  print("Summary: " + json_res['daily']['data'][0]['summary'])
  precip_type = None
  precip_prob = None
  if'precipProbability' in json_res['daily']['data'][0] and 'precipType' in json_res['daily']['data'][0]:
    precip_type = json_res['daily']['data'][0]['precipType']
    precip_prob = json_res['daily']['data'][0]['precipProbability']
  if (precip_type == 'rain' and precip_prob != None):
    precip_prob *= 100
    print("Chance of rain: %.2f%%" % (precip_prob))



canvas1 = tk.Canvas(root,bg="DeepSkyBlue2",width=0,height=50 )
canvas1.place(x=200,y=550)

#==============================================================================
icon_id = DAY_TYPE[0]  #json_res['daily']['data'][0]['icon']
icon2 = None
if icon_id in icon_lookup:
    icon2 = icon_lookup[icon_id]
    print(icon2)  

load2 = Image.open(basepath+icon2)
print(basepath+icon2)
load2 = load2.resize((100,100))
render2 = ImageTk.PhotoImage(load2)
day1_img = tk.Label(root,image=render2,bg="DeepSkyBlue2",fg="white")
day1_img.place(x=250,y=500)

day1 = tk.Label(root,text = str(MIN_TEMP[0])+'°C-'+str(MAX_TEMP[0])+'°C',font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
day1.place(x=250,y=620)

import datetime  
from datetime import date 
date=str(future_dates[0].replace('-',' '))
month, day, year = date.split(' ')     
day_name = datetime.date(int(year), int(month), int(day)) 
print(day_name.strftime("%A")) 

WAR1 = tk.Label(root,text = str(day_name.strftime("%A")[:3]),font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
WAR1.place(x=250,y=450)
#==============================================================================

icon_id = DAY_TYPE[1]  #json_res['daily']['data'][0]['icon']
icon2 = None
if icon_id in icon_lookup:
    icon2 = icon_lookup[icon_id]
    print(icon2)  

load3 = Image.open(basepath+icon2)
print(basepath+icon2)
load3 = load3.resize((100,100))
render3 = ImageTk.PhotoImage(load3)
day1_img = tk.Label(root,image=render3,bg="DeepSkyBlue2",fg="white")
day1_img.place(x=400,y=500)

day2 = tk.Label(root,text = str(MIN_TEMP[1])+'°C-'+str(MAX_TEMP[1])+'°C',font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
day2.place(x=400,y=620)

date=str(future_dates[1].replace('-',' '))
month, day, year = date.split(' ')     
day_name = datetime.date(int(year), int(month), int(day)) 
print(day_name.strftime("%A")) 

WAR2 = tk.Label(root,text = str(day_name.strftime("%A")[:3]),font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
WAR2.place(x=400,y=450)

#==============================================================================

icon_id = DAY_TYPE[2]  #json_res['daily']['data'][0]['icon']
icon2 = None
if icon_id in icon_lookup:
    icon2 = icon_lookup[icon_id]
    print(icon2)  

load4 = Image.open(basepath+icon2)
print(basepath+icon2)
load4 = load3.resize((100,100))
render4 = ImageTk.PhotoImage(load4)
day1_img = tk.Label(root,image=render4,bg="DeepSkyBlue2",fg="white")
day1_img.place(x=550,y=500)

day3 = tk.Label(root,text = str(MIN_TEMP[2])+'°C-'+str(MAX_TEMP[2])+'°C',font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
day3.place(x=550,y=620)

date=str(future_dates[2].replace('-',' '))
month, day, year = date.split(' ')     
day_name = datetime.date(int(year), int(month), int(day)) 
print(day_name.strftime("%A")) 

WAR3 = tk.Label(root,text = str(day_name.strftime("%A")[:3]),font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
WAR3.place(x=550,y=450)

#==============================================================================

icon_id = DAY_TYPE[3]  #json_res['daily']['data'][0]['icon']
icon2 = None
if icon_id in icon_lookup:
    icon2 = icon_lookup[icon_id]
    print(icon2)  

load5 = Image.open(basepath+icon2)
print(basepath+icon2)
load5 = load5.resize((100,100))
render5 = ImageTk.PhotoImage(load5)
day1_img = tk.Label(root,image=render5,bg="DeepSkyBlue2",fg="white")
day1_img.place(x=700,y=500)

day4 = tk.Label(root,text = str(MIN_TEMP[3])+'°C-'+str(MAX_TEMP[3])+'°C',font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
day4.place(x=700,y=620)

date=str(future_dates[3].replace('-',' '))
month, day, year = date.split(' ')     
day_name = datetime.date(int(year), int(month), int(day)) 
print(day_name.strftime("%A")) 

WAR4 = tk.Label(root,text = str(day_name.strftime("%A")[:3]),font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
WAR4.place(x=700,y=450)

#==============================================================================

icon_id = DAY_TYPE[4]  #json_res['daily']['data'][0]['icon']
icon2 = None
if icon_id in icon_lookup:
    icon2 = icon_lookup[icon_id]
    print(icon2)  

load6 = Image.open(basepath+icon2)
print(basepath+icon2)
load6 = load3.resize((100,100))
render6 = ImageTk.PhotoImage(load6)
day1_img = tk.Label(root,image=render6,bg="DeepSkyBlue2",fg="white")
day1_img.place(x=850,y=500)

day5 = tk.Label(root,text = str(MIN_TEMP[4])+'°C-'+str(MAX_TEMP[4])+'°C',font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
day5.place(x=850,y=620)

date=str(future_dates[4].replace('-',' '))
month, day, year = date.split(' ')     
day_name = datetime.date(int(year), int(month), int(day)) 
print(day_name.strftime("%A")) 

WAR5 = tk.Label(root,text = str(day_name.strftime("%A")[:3]),font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
WAR5.place(x=850,y=450)
#==============================================================================

icon_id = DAY_TYPE[5]  #json_res['daily']['data'][0]['icon']
icon2 = None
if icon_id in icon_lookup:
    icon2 = icon_lookup[icon_id]
    print(icon2)  

load7 = Image.open(basepath+icon2)
print(basepath+icon2)
load7 = load3.resize((100,100))
render7 = ImageTk.PhotoImage(load7)
day1_img = tk.Label(root,image=render7,bg="DeepSkyBlue2",fg="white")
day1_img.place(x=1000,y=500)

day6 = tk.Label(root,text = str(MIN_TEMP[5])+'°C-'+str(MAX_TEMP[5])+'°C',font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
day6.place(x=1000,y=620)

date=str(future_dates[5].replace('-',' '))
month, day, year = date.split(' ')     
day_name = datetime.date(int(year), int(month), int(day)) 
print(day_name.strftime("%A")) 

WAR6 = tk.Label(root,text = str(day_name.strftime("%A")[:3]),font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
WAR6.place(x=1000,y=450)
#==============================================================================


icon_id = DAY_TYPE[6]  #json_res['daily']['data'][0]['icon']
icon2 = None
if icon_id in icon_lookup:
    icon2 = icon_lookup[icon_id]
    print(icon2)  

load8 = Image.open(basepath+icon2)
print(basepath+icon2)
load8 = load3.resize((100,100))
render8 = ImageTk.PhotoImage(load8)
day1_img = tk.Label(root,image=render8,bg="DeepSkyBlue2",fg="white")
day1_img.place(x=1150,y=500)

day7 = tk.Label(root,text = str(MIN_TEMP[6])+'°C-'+str(MAX_TEMP[6])+'°C',font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
day7.place(x=1150,y=620)

date=str(future_dates[6].replace('-',' '))
month, day, year = date.split(' ')     
day_name = datetime.date(int(year), int(month), int(day)) 
print(day_name.strftime("%A")) 

WAR7 = tk.Label(root,text = str(day_name.strftime("%A")[:3]),font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
WAR7.place(x=1150,y=450)





import requests 
api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="

import json
location_req_url='http://api.ipstack.com/103.51.95.183?access_key=fcdaeccb61637a12fdf64626569efab0'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)

lat = location_obj['latitude']
lon = location_obj['longitude']

location2 = "%s, %s" % (location_obj['city'], location_obj['region_code'])
location2 = location2.replace(',','')
print(location2.split()[0])
city =location2.split()[0] 
url = api_address + city
json_data = requests.get(url).json()

P = json_data['main']['pressure']
H = json_data['main']['humidity']
W = json_data['wind']['speed']

C_T = json_data['main']['temp']/10




P_label = tk.Label(root,text ="Pressure : "+ str(P)+" mbar",font=("Times New Roman",22),bg="DeepSkyBlue2",fg="white")
P_label.place(x=80,y=150)


H_label = tk.Label(root,text ="Humidity : "+ str(H)+" %",font=("Times New Roman",22),bg="DeepSkyBlue2",fg="white")
H_label.place(x=80,y=220)


W_label = tk.Label(root,text ="Wind Speed : "+ str(W)+"m/s",font=("Times New Roman",22),bg="DeepSkyBlue2",fg="white")
W_label.place(x=80,y=290)



canvas2 = tk.Canvas(root,bg="DeepSkyBlue2",width=0)
canvas2.place(x=400,y=120)








DEGREE_SIGN = u'\N{DEGREE SIGN}'

ui_locale = '' # e.g. 'fr_FR' fro French, '' as default
time_format = 12 # 12 or 24
date_format = "%b %d, %Y" # check python doc for strftime() for options
news_country_code = 'in'
weather_api_token = '2981c8ba16e53d981a8e78b3e2953ca1'    #'<TOKEN>' # create account at https://darksky.net/dev/
weather_lang = 'en' # see https://darksky.net/dev/docs/forecast for full list of language parameters values
weather_unit = 'auto' # see https://darksky.net/dev/docs/forecast for full list of unit parameters values

weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s?lang=%s&units=%s" % (weather_api_token, lat,lon,weather_lang,weather_unit)

r = requests.get(weather_req_url)
weather_obj = json.loads(r.text)

degree_sign= u'\N{DEGREE SIGN}'
temperature2 = "%s%s" % (str(int(weather_obj['currently']['temperature'])), degree_sign)
currently2 = weather_obj['currently']['summary']
forecast2 = weather_obj["hourly"]["summary"]


from datetime import date
import calendar
my_date = date.today()
day = calendar.day_name[my_date.weekday()]  #'Wednes
print(day)

current_temp_label = tk.Label(root,text = str(temperature2)+' C\n'+str(day[:3]),font=("Times New Roman",42),bg="DeepSkyBlue2",fg="white",height=3)
current_temp_label.place(x=22,y=490)


from datetime import datetime
TODAY = datetime.today().strftime("%Y-%m-%d")
TODAY = TODAY+"T00:00:00"
response = requests.get("https://api.darksky.net/forecast/2981c8ba16e53d981a8e78b3e2953ca1/"+str(latitude)+","+str(longitude)+","+str(TODAY)+"?"+str(option_list))
json_res = response.json()
today_min_temp = (json_res['daily']['data'][0]['apparentTemperatureMin']-32) * 5/9
today_max_temp = (json_res['daily']['data'][0]['apparentTemperatureMax']-32) * 5/9

canvas3 = tk.Canvas(root,bg="DeepSkyBlue2",width=0)
canvas3.place(x=850,y=120)


C_MN_T = tk.Label(root,text = "Min. Temp.\n"+str(today_min_temp)[:2]+'°C',font=("Times New Roman",30),bg="DeepSkyBlue2",fg="white",height=3)
C_MN_T.place(x=950,y=130)

C_MX_T = tk.Label(root,text = "Max. Temp.\n"+str(today_max_temp)[:2]+'°C',font=("Times New Roman",30),bg="DeepSkyBlue2",fg="white",height=3)
C_MX_T.place(x=950,y=250)


icon_id = weather_obj['currently']['icon']
icon2 = None

if icon_id in icon_lookup:
    icon2 = icon_lookup[icon_id]
    print(icon2)

basepath = "c:/Weather_Forecast_Crop_Suggestion/"
from PIL import Image , ImageTk
load1 = Image.open(basepath+str(icon2))
load1 = load1.resize((200,200))
render1 = ImageTk.PhotoImage(load1)
    
IMAGE_LABEL = tk.Label(root,image=render1,bg="DeepSkyBlue2",fg="white")
IMAGE_LABEL.place(x=500,y=140)

location_label = tk.Label(root,text=str(location2),font=("Times New Roman",35),bg="DeepSkyBlue2",fg="white")
location_label.place(x=500,y=60)

status = tk.Label(root,text=': '+str(icon_id)+" :",font=("Times New Roman",20),bg="DeepSkyBlue2",fg="white")
status.place(x=475,y=375)


def CROP_SUGG():
    root.destroy()
    from subprocess import call
    call(["python","Soil_Testing.py"])

soil = tk.Button(root,text="$0!l",width=5,font=("Times",10),bg="DeepSkyBlue2",fg="white",command=CROP_SUGG)
soil.place(x=5,y=5)

root.mainloop()