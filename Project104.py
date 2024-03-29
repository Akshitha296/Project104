import csv
from collections import Counter

with open('SOCR-HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))

n = len(new_data)
total = 0

for x in new_data:
    total += x

mean = total/n

with open('SOCR-HeightWeight.csv', newline = '') as q:
    reader = csv.reader(q)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for w in range(len(file_data)):
    num = file_data[w][1]
    new_data.append(float(num))

new_data.sort()
numb = len(new_data)

if numb%2 == 0:
    median1 = float(new_data[numb//2])
    median2 = float(new_data[numb//2-1])
    median = (median1+median2)/2
else:
    median = new_data[numb//2]

with open('SOCR-HeightWeight.csv', newline = '') as e:
    reader = csv.reader(e)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for r in range(len(file_data)):
    num = file_data[r][1]
    new_data.append(float(num))

data = Counter(new_data)
mode_data_for_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

for height, occurence in data.items():
    if 50 < float(height)<60:
        mode_data_for_range["50-60"]+= occurence
    elif 60 < float(height)<70:
        mode_data_for_range["60-70"]+= occurence
    elif 70 < float(height)<80:
        mode_data_for_range["70-80"]+= occurence

mode_range, mode_occurence = 0,0

for range, occurence in mode_data_for_range.items():
    if occurence>mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((mode_range[0]+mode_range[1])/2)

print("Mean is --> " + str(mean))
print("Median is --> " + str(median))
print("Mode is --> " + str(mode))