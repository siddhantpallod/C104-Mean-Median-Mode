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
newData.sort()

if l % 2 == 0:
    median1 = float(newData[l//2])
    median2 = float(newData[l//2-1])
    median = (median1 + median2) / 2

else:
    median = newData[l//2]

print(median)