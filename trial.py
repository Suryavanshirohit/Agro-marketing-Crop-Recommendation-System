import requests 
api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="

#api.openweathermap.org/data/2.5/forecast?id=524901      Weather forecasting by CITY ID


import json
location_req_url='http://api.ipstack.com/103.51.95.183?access_key=fcdaeccb61637a12fdf64626569efab0'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)

lat = location_obj['latitude']
lon = location_obj['longitude']
latitude = lat
longitude = lon

#api_address = "http://api.openweathermap.org/data/2.5/forecast?appid=0c42f7f6b53b244c78a418f4f181282a&q=lat='{}'&lon='{}'".format(lat,lon)

location2 = "%s, %s" % (location_obj['city'], location_obj['region_code'])
location2 = location2.replace(',','')
print(location2.split()[0])
city =location2.split()[0] 
#city="Nagpur"
url = api_address + city
#url = api_address + 'Mumbai'
json_data = requests.get(url).json()
print(json_data['main']['temp'])
temp = json_data['main']['temp']
print(json_data['sys']['country'])
print(json_data['name'])
temp = temp-273.15
print(temp)


from datetime import datetime
TODAY = datetime.today().strftime("%Y-%m-%d")
TODAY = TODAY+"T00:00:00"
option_list = "exclude=currently,minutely,hourly,alerts&amp;units=si"
response = requests.get("https://api.darksky.net/forecast/2981c8ba16e53d981a8e78b3e2953ca1/"+str(latitude)+","+str(longitude)+","+str(TODAY)+"?"+str(option_list))
json_res = response.json()
today_min_temp = (json_res['daily']['data'][0]['apparentTemperatureMin']-32) * 5/9
today_max_temp = (json_res['daily']['data'][0]['apparentTemperatureMax']-32) * 5/9

MN = (json_res['daily']['data'][0]['apparentTemperatureMin']-32) * 5/9
MX = (json_res['daily']['data'][0]['apparentTemperatureMax']-32) * 5/9


ans= 'BLACK'
crop = {'BLACK':['Soyabean','Sorghum','Jowar','Millet','Linseed','Castor','Safflower'],'CLAY':['Broccoli','Sprouts','Cabbage','Bean','Potato','Corn','Rice'],'RED':['Groundnut','Cashew','Banana','Maize','Soyabean','Jute','Bajra'],'SANDY':['Carrot','Potato','Lettuce','Peppers','Maize','Tomato']}

crop[ans]


Temp_data = {'Rice':'20-27','Wheat':'15-25','SugarCane':'20-26','Tobacco':'20-30','Cotton':'20-28','Oilseeds':'20-30','Jute':'24-38','Maize':'18-27','Soyabean':'21-35','Sorghum':'25-30','Jowar':'27-32','Millet':'25-30','Linseed':'10-38','Castor':'15-20',
'Safflower':'22-35','Broccoli':'10-20','Sprouts':'23-29','Cabbage':'15-20','Bean':'20-25','Potato':'15-20','Corn':'25-32','Groundnut':'21-35','Cashew':'25-40','Banana':'15-35','Bajra':'20-30','Carrot':'15-20','Lettuce':'15-25','Peppers':'20-25','Tomato':'18-29'}

#Linseed/Javas
possible_crops = crop[ans]


got_crops = []
for i in range(len(possible_crops)):
    if int(temp) in range(int(Temp_data[possible_crops[i]][:2]),int(Temp_data[possible_crops[i]][3:5])):
        print(int(Temp_data[possible_crops[i]][:2]),int(Temp_data[possible_crops[i]][3:5]))
        print(possible_crops[i])
        got_crops.append(possible_crops[i])




print("1st Stage",got_crops)




MN = int(MN)
MX = int(MX)
got_more_crops = []
for i in range(len(possible_crops)):
    for j in range(MN,MX):
        if int(j) in range(int(Temp_data[possible_crops[i]][:2]),int(Temp_data[possible_crops[i]][3:5])):
            #print(int(Temp_data[possible_crops[i]][:2]),int(Temp_data[possible_crops[i]][3:5]))
            #print(possible_crops[i])
            got_more_crops.append(possible_crops[i])

print("Second Stage",set(got_more_crops))

for j in range(MN,MX):
    print(j)