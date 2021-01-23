import csv
from collections import Counter

with open('height.csv', newline = '') as a:
    readData = csv.reader(a)
    fileData = list(readData)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))

data = Counter(newData)
dataRange = {
    '50-60' : 0,
    '60-70' : 0,
    '70-80' : 0
}

for height, occurence in data.items():
    if 50 < float(height) < 60:
        dataRange['50-60'] += occurence
    elif 60 < float(height) < 70:
        dataRange['60-70'] += occurence
    elif 70 < float(height) < 80:
        dataRange['70-80'] += occurence

modeRange, modeOccurence = 0,0

for range, occurence in dataRange.items():
    if occurence > modeOccurence:
        modeRange, modeOccurence = [int(range.split('-')[0]), int(range.split('-')[1])], occurence

mode = float((modeRange[0] + modeRange[1]) /2)

print(mode)