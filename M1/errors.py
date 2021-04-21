csv_file = open("csv.txt","r")
csv_content = csv_file.readlines()
csv_file.close()
print(csv_content)

for i in csv_content:
    print(i)