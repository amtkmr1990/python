
with open('csv.txt') as mycsv:
    file = mycsv.readlines()

json = []
for l in file:
    dict= {
        'club' :  l.strip().split(',')[0],
        'city' : l.strip().split(',')[1],
        'state' : l.strip().split(',')[2]
        }
    json.append(dict)
print(json)