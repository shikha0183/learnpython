import json
json_list = []

csv_file = open('csv_data.txt', 'r')
lines = csv_file.readlines()




lines = [line.strip() for line in lines[1:]]

for line in lines:
    name,age,university,degree = line.split(',')
    data = {
        'name': name,
        'age': age,
        'university': university,
        'degree': degree

    }
    json_list.append(data)

csv_file.close()

json_file = open('json_file.txt','w')
json.dump(json_list,json_file)
json_file.close()


