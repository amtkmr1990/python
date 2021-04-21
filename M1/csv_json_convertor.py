"""
read the content of csv file
create a dictionary
add keys and values from csv file
convert dictionary to json dump
"""
import json

club_details = []

csv_file = open("csv.txt","r")
csv_content = csv_file.readlines()
csv_file.close()
for i in csv_content:
    club, city, country = i.strip().split(",")
    data = {'club': club, 'city': city, 'country': country}
    club_details.append(data)


load_file = open("club_json_details.txt","w")
json.dump(club_details,load_file)
load_file.close()

print(club_details)