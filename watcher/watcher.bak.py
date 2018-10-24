# Prograam to watch if cats aroudn

import requests, json, ast
from picamera import PiCamera
from time import sleep
from playsound import playsound
from datetime import datetime
import os

print('Starting...')

# sleep(30.)

camera = PiCamera()

while True:
    
    try:
        # file name
        dateStamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = '/home/pi/picsCatDetector/picture_{}.jpg'.format(dateStamp)  

        # Take picture
        camera.start_preview()
        camera.capture(file_name)
        camera.stop_preview()

        url = 'http://0.0.0.0:5000/api'
        url = 'http://35.200.240.45:80/api'
        files = {'image': open(file_name, 'rb')}
        r = requests.post(url, files=files)
        print(r.text)

        dicOut = ast.literal_eval(r.text)
        proba = dicOut['probaCat']
        
        print("Probability = {}".format(proba))
        
        if proba > 0.98:
            os.system('mpg123 vaccum1.mp3')
            file_name2 = file_name.split('.')[0] + str('_') + str(proba) + '.jpg'
            print(file_name2)
            os.rename(file_name, file_name2)
        else:
            os.remove(file_name)
    except:
        print("Error")
    
    


