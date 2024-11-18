import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
# import sys
from PIL import Image, ImageTk
import PIL.Image
import cv2
import tflearn
import numpy as np
import tensorflow as tf
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression


import warnings
warnings.filterwarnings('ignore') # suppress import warnings

root=tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background="cyan3")

root.title(" "*190+"---CROP DETECTION---")


#####For background Image
image2 = Image.open('cor1.jpg')
image2 = image2.resize((1400, 1400), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

   # l = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="#192841", fg="white")
   # l.place(x=190, y=50)




lbl = tk.Label(root, text="Crop Prediction System Using ML", font=('times', 35,' bold '), height=1, width=52,bg="#004340",fg="white")
lbl.place(x=0, y=0)

IMG_SIZE = 50
LR = 1e-3
#MODEL_NAME = 'lungdetection-{}-{}.model'.format(LR, '2conv-basic')
MODEL_NAME = 'soilclassification-{}-{}.model'.format(LR, '2conv-basic')

#tf.logging.set_verbosity(tf.logging.ERROR) # suppress keep_dims warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # suppress tensorflow gpu logs
IMAGE_SIZE = 64
def openphoto():
    #dirPath = "test/test"
    #fileList = os.listdir(dirPath)
    # for fileName in fileList:
    #     os.remove(dirPath + "/" + fileName)
    #P_th = 'F:/project/breath_detection/breath_project/train/train'
    fileName = askopenfilename( title='Select image for analysis ',
                              filetypes=[('All files', '*.*'), ('image files', '.jpeg')])

    imgpath = fileName

    load = PIL.Image.open(fileName)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root, image=render, height="250", width="250",bg="white")
    img.image = render
    img.place(x=380, y=80)
    
   
    
    gs = cv2.cvtColor(cv2.imread(imgpath, 1), cv2.COLOR_RGB2GRAY)
    x1 = int(gs.shape[0] / 2)
    y1 = int(gs.shape[1] / 2)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
    #result_label1.place(x=300, y=400)
    img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=680, y=80)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=980, y=80)




    """
    gs = cv2.cvtColor(cv2.imread(imgpath, 1), cv2.COLOR_RGB2GRAY)
    x1 = int(gs.shape[0] / 2)
    y1 = int(gs.shape[1] / 2)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    """

    f=fileName.split("/").pop()
    f=f.split(".").pop(0)
    print(fileName)
    print(f)
    filepath=fileName

    def process_verify_data(filepath):

        verifying_data = []

        img_name = filepath.split('.')[0]
        img = cv2.imread(filepath, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        verifying_data = [np.array(img), img_name]

        #np.save('verify_data.npy', verifying_data)
        np.save('verify_data - Copy.npy', verifying_data)
        

        return verifying_data

    def analysis(filepath):

        verify_data = process_verify_data(filepath)

        str_label = "Cannot make a prediction."
        status = "Error"

#        tf.reset_default_graph()

        convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 3], name='input')

        convnet = conv_2d(convnet, 32, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 64, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 128, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 32, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 64, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = fully_connected(convnet, 1024, activation='relu')
        convnet = dropout(convnet, 0.8)

        convnet = fully_connected(convnet, 4, activation='softmax')
        convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy',
                             name='targets')

        model = tflearn.DNN(convnet, tensorboard_dir='log')


        if os.path.exists('{}.meta'.format(MODEL_NAME)):
            model.load(MODEL_NAME)
            print('Model loaded successfully.')
#            load=tk.Label(root,text="Model Loaded Successfully",width=30,height=2,font=("Tempus Sans ITC", 13, "bold"),background="red",foreground="white")
#            load.place(x=350,y=455)
        else:
            print('Error: Create a model using neural_network.py first.')
#            Uload=tk.Label(root,text='Error: Create a model using neural_network.py first.',width=30,height=2,font=("Tempus Sans ITC", 13, "bold"),background="red",foreground="white")
#            Uload.place(x=350,y=455)
        img_data, img_name = verify_data[0], verify_data[1]

        orig = img_data
        data = img_data.reshape(IMG_SIZE, IMG_SIZE, 3)


        
        model_out = model.predict([data])[0]
        print(np.argmax(model_out))
        if np.argmax(model_out) == 0:
            str_label = 'BLACK'
        elif np.argmax(model_out) == 1:
            str_label = 'CLAY'
        elif np.argmax(model_out) == 2:
            str_label = 'RED'
        elif np.argmax(model_out) == 3:
            str_label = 'SANDY'

        #if str_label == 'Healthy':
         #   status = 'Healthy'
        #else:
        
        dis = tk.Label(root,text="On the basis of image Soil type "+str(str_label)+" is Detected",font=('Tempus Sanc ITC',25,'italic'),bg='#00A79F',fg="black")        
        dis.place(x=500,y=350)
        #Disease=tk.Label(root,text=str(str_label),width=20,height=2,font=("Tempus Sans ITC",25,"bold"),background="cyan3",foreground="red4")
        #Disease.place(x=450,y=600)
        
        print(str_label)
        
        import requests 
        api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
        
        import json
        location_req_url='http://api.ipstack.com/103.51.95.183?access_key=fcdaeccb61637a12fdf64626569efab0'
        r = requests.get(location_req_url)
        location_obj = json.loads(r.text)
        
        lat = location_obj['latitude']
        lon = location_obj['longitude']
        latitude = lat
        longitude = lon
        
        
        location2 = "%s, %s" % (location_obj['city'], location_obj['region_code'])
        location2 = location2.replace(',','')
        print(location2.split()[0])
        city =location2.split()[0] 
        
        location_label = tk.Label(root,text="At location  "+str(location2),font=('Times New Roman',35,'italic'),bg="#00A79F",fg="white")
        location_label.place(x=650,y=580)
        
        url = api_address + city
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
        
        MN = today_min_temp
        MX = today_max_temp
        
        head0 = tk.Label(root,text="Temprature",font=('Tempus Sanc ITC',25,'italic'),bg='#00A79F',fg="black")        
        head0.place(x=80,y=350)
        
        #canvas1 = tk.Canvas(root,bg="DeepSkyBlue2",width=500,height=0)
        #canvas1.place(x=300,y=300)
        
        MN_label = tk.Label(root,text="Min. Temp.\n"+str(MN)[:2]+'°C',font=('Tempus Sanc ITC',20,'italic'),bg='#00A79F',fg="white")        
        MN_label.place(x=100,y=400)
        
        MX_label = tk.Label(root,text="Max. Temp.\n"+str(MX)[:2]+'°C',font=('Tempus Sanc ITC',20,'italic'),bg='#00A79F',fg="white")        
        MX_label.place(x=100,y=500)
        
        #canvas2 = tk.Canvas(root,bg="DeepSkyBlue2",width=500,height=0)
        #canvas2.place(x=650,y=320)
        
        #ans= 'BLACK'
        ans = str_label
        #ans = 'SANDY'
        crop = {'BLACK':['Soyabean','Sorghum','Jowar','Millet','Linseed','Castor','Safflower'],'CLAY':['Broccoli','Sprouts','Cabbage','Bean','Potato','Corn','Rice'],'RED':['Groundnut','Cashew','Banana','Maize','Soyabean','Jute','Bajra'],'SANDY':['Carrot','Potato','Lettuce','Peppers','Maize','Tomato']}
        
        crop[ans]
        
        
        Temp_data = {'Rice':'20-27','Wheat':'15-25','SugarCane':'20-26','Tobacco':'20-30','Cotton':'20-28','Oilseeds':'20-30','Jute':'24-38','Maize':'18-27','Soyabean':'21-35','Sorghum':'25-30','Jowar':'27-32','Millet':'25-30','Linseed':'10-38','Castor':'15-20',
        'Safflower':'22-35','Broccoli':'10-20','Sprouts':'23-29','Cabbage':'15-20','Bean':'20-25','Potato':'15-20','Corn':'25-32','Groundnut':'21-35','Cashew':'25-40','Banana':'15-35','Bajra':'20-30','Carrot':'15-20','Lettuce':'15-25','Peppers':'20-25','Tomato':'18-29'}
        
        VALUE_DATA = {'Broccoli':'E:/crop_prediction/PRICE_DATA/BROCCOLI.csv','Carrot':'E:/crop_prediction/PRICE_DATA/CARROT.csv','Cotton':'E:/crop_prediction/PRICE_DATA/COTTON.csv','Peppers':'E:/crop_prediction/PRICE_DATA/PEPPER.csv','Potato':'E:/crop_prediction/PRICE_DATA/POTATO.csv','Rice':'E:/crop_prediction/PRICE_DATA/RICE.csv','SugarCane':'E:/crop_prediction/PRICE_DATA/SUGARCANE.csv','Tomato':'E:/crop_prediction/PRICE_DATA/TOMATO.csv','Wheat':'E:/crop_prediction/PRICE_DATA/WHEAT.csv'}          
        
        #Linseed/Javas
        possible_crops = crop[ans]
        
        """
        got_crops = []
        for i in range(len(possible_crops)):
            if int(temp) in range(int(Temp_data[possible_crops[i]][:2]),int(Temp_data[possible_crops[i]][3:5])):
                print(int(Temp_data[possible_crops[i]][:2]),int(Temp_data[possible_crops[i]][3:5]))
                print(possible_crops[i])
                got_crops.append(possible_crops[i])
        """
        
        
        
        print("1st Stage",possible_crops)
        
        head1 = tk.Label(root,text="<<<Crops Based on Soil Type>>>",width=30,font=('Tempus Sanc ITC',25,'italic'),bg='#00A79F',fg="white")        
        head1.place(x=600,y=450)
        crop1 = tk.Label(root,text=str(set(possible_crops)),width=50,font=('Tempus Sanc ITC',20,'italic'),bg='#00A79F',fg="white")        
        crop1.place(x=500,y=500)
        
        
        MN = int(MN)
        MX = int(MX)
        #MN = int(20)
        #MX = int(35)
        got_more_crops = []
        for i in range(len(possible_crops)):
            for j in range(MN,MX):
                if int(j) in range(int(Temp_data[possible_crops[i]][:2]),int(Temp_data[possible_crops[i]][3:5])):
                    #print(int(Temp_data[possible_crops[i]][:2]),int(Temp_data[possible_crops[i]][3:5]))
                    #print(possible_crops[i])
                    got_more_crops.append(possible_crops[i])
        
        print("Second Stage",set(got_more_crops))
        got_more_crops = list(set(got_more_crops))
        to_know = []
        key_price = []            
        PATHS = []
        forecasted_values = {}
        for values in VALUE_DATA:
            print(values)
            to_know.append(values)
        print(set(got_more_crops)&set(to_know))
        key_price.extend(list(set(got_more_crops)&set(to_know)))
        for k in key_price:
            print(VALUE_DATA[k])
            PATHS.append(VALUE_DATA[k])
        #x = 'E:/Soil_Crop_Suggestion/PRICE_DATA/PEPPER.csv'
        from CROP_PRICING import FORECAST
        for x in PATHS:
            FORECAST(x)
            forecasted_values[str(x.split('.')[0].split('/')[-1])] = (FORECAST(x))
            
        print(forecasted_values)
        
        
        
        
        #+'\n'+str(forecasted_values)
        head2 = tk.Label(root,text="<<<Crops Based on Soil Type and Weather>>>",width=35,font=('Tempus Sanc ITC',15,'italic'),bg='#00A79F',fg="white")        
        head2.place(x=50,y=500)
        crop2 = tk.Label(root,text=str(set(got_more_crops)),width=50,font=('Tempus Sanc ITC',15,'italic'),bg='#00A79F',fg="white")        
        crop2.place(x=600,y=500)
        return str_label
    
    
    

    analysis(filepath)


def KILL():
    root.destroy()
    from subprocess import call
    call(["python","Weather_Screen.py"])

button1 = tk.Button(root, text="Browse Photo", command = openphoto,width=30,height=2,font=("Tempus Sans ITC", 13, "bold"),fg="white",background="#B40000")
button1.grid(column=0, row=1, padx=10, pady = 10)
button1.place(x=50,y=100)


exit =  tk.Button(root, text="Exit", command = KILL,width=30,height=2,font=("Tempus Sans ITC", 13, "bold"),fg="white",background="#B40000")
exit.place(x=50,y=200)




root.mainloop()