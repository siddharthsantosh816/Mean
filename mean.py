import csv
from collections import Counter

with open('C:/Users/w/Desktop/Python/csv/SOCR-HeightWeight.csv') as f:
    reader=csv.reader(f)
    new_data=list(reader)


new_data.pop(0)
weight_data=[]

for i in range(len(new_data)):
    n_num=new_data[i][2]
    weight_data.append(float(n_num))

# MEAN

mean=sum(weight_data)/len(weight_data)
print("The mean is "+str(mean))


# MEDIAN

weight_data.sort()
n=len(weight_data)

if n%2==0:
    median1=float(weight_data[n//2])
    median2=float(weight_data[n//2-1])
    median=(median1+median2)/2

else:
    median=weight_data[n//2]

print("Median is: "+str(median))

# MODE
data=Counter(weight_data)
mode_range = {
    '75-85':0,
    '85-95':0,
    '95-105':0,
    '105-115':0,
    '115-125':0,
    '125-135':0,
    '135-145':0,
    '145-155':0,
    '155-165':0,
    '165-175':0
}

for weight,occurance in data.items():
    if 75<float(weight)<85:
        mode_range['75-85']+=occurance
    elif 85<float(weight)<95:
        mode_range['85-95']+=occurance
    elif 95<float(weight)<105:
        mode_range['95-105']+=occurance
    elif 105<float(weight)<115:
        mode_range['105-115']+=occurance
    elif 115<float(weight)<125:
        mode_range['115-125']+=occurance
    elif 125<float(weight)<135:
        mode_range['125-135']+=occurance
    elif 135<float(weight)<145:
        mode_range['135-145']+=occurance
    elif 145<float(weight)<155:
        mode_range['145-155']+=occurance
    elif 155<float(weight)<165:
        mode_range['155-165']+=occurance
    else:
        mode_range['165-175']+=occurance

# print(mode_range)
range,occ=0,0
for r,o in mode_range.items():
    if o>occ:
        range,occ=[int(r.split("-")[0]), int(r.split("-")[1])], o
        
mode = float((range[0] + range[1]) / 2)
print("Mode is "+str(mode))
