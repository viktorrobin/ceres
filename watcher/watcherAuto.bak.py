#!/usr/bin/env python
# /etc/init.d/sample.py
### BEGIN INIT INFO
# Provides:          watcherAuto.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

import requests, json, ast
from picamera import PiCamera
from time import sleep
from playsound import playsound
from datetime import datetime

camera = PiCamera()

while True:
    
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

    if proba > 0.95:
        playsound('vaccum1.mp3')
