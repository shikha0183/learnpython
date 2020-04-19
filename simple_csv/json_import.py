import json

file = open("friends_json.txt", "r")
file_contents = json.load(file)

file.close()

print(file_contents['friends'][2])

cars = [

    {"make": 'Ford', "model": 'Fiesta'},
    {"make": 'Ford', "model": 'Focus'}
]

file = open('cars_json.txt','w')
json.dump(cars,file)
file.close()
