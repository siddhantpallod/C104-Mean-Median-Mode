import csv

with open('height.csv', newline = '') as a:
    readData = csv.reader(a)
    fileData = list(readData)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))

l = len(newData)
total = 0

for a in newData:
    total += a

mean = total/l

print(mean)