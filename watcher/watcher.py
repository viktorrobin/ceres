# Call flask API


# curl -i http://localhost:5000/api/catEatingPlan2.jpg

import requests, json, ast

# r = requests.get('http://localhost:5000/api/catEatingPlan2.jpg')
file_name = 'catEatingPlan2.jpg'
r = requests.post('http://localhost:5000/api/{}'.format(file_name))
print(r.text)

dicOut = ast.literal_eval(r.text)
proba = dicOut['probaCat']

if proba > 0.5:
    from playsound import playsound
    playsound('vaccum1.mp3')