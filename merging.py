import csv

dataset_1 = []
data_sorted = []

with open("dataset_1.csv", "r") as f:
    c = csv.reader(f)
    for i in c :
        dataset_1.append(i)

with open("dataset_2_sorted.csv", "r") as f:
    c = csv.reader(f)
    for i in c :
        data_sorted.append(i)
        
header1  = dataset_1[0]
planet_data_1  = dataset_1[1:]

header2  = data_sorted[0]
planet_data_2  = data_sorted[1:]

header = header1 + header2
final_planet_data = []

for index,item in enumerate(planet_data_1):
    final_planet_data.append(planet_data_1[index] + planet_data_2[index])
    
with open("final_data.csv","a+") as f:
    c = csv.writer(f)
    c.writerow(header)
    c.writerows(final_planet_data)