import csv

data = []
with open("dataset_2.csv","r") as f :
    c = csv.reader(f)
    for i in c :
        data.append(i)
headers = data[0]
planet_data = data[1:]
#Converting all planet names to lower case
for j in planet_data:
    j[2] = j[2].lower()
    
planet_data.sort(key = lambda  planet_data : planet_data[2])


with open("dataset_2_sorted.csv","a+") as f :
    c = csv.writer(f)
    c.writerow(headers)
    c.writerows(planet_data)