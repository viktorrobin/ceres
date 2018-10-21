# Call flask API
import requests, json, ast

file_name = 'catEatingPlan2.jpg'
file_name = 'file.jpeg'

url = 'http://0.0.0.0:5000/api'
url = 'http://35.200.240.45:80/api'
files = {'image': open(file_name, 'rb')}
r = requests.post(url, files=files)
print(r.text)


if 0:
    # curl -i http://localhost:5000/api/catEatingPlan2.jpg
    # r = requests.get('http://localhost:5000/api/catEatingPlan2.jpg')
    

    r = requests.post('http://localhost:5000/api/{}'.format(file_name))
    print(r.text)

    dicOut = ast.literal_eval(r.text)
    proba = dicOut['probaCat']

    if proba > 0.5:
        from playsound import playsound
        playsound('vaccum1.mp3')