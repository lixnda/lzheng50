"""
Linda Zheng
Boas
SoftDev
K<05> -- Bitstream
2024-09-17
time spent: 0.5

Issues: would not work if names had space in them due to string parcings (FIXED)
"""

import random

file = open("krewes.txt", "r")
krewes = {}

data=file.read()

data = data.replace("@", "$")
outputdata = ""
for i in range(len(data) -1):
    if not(i != 0 and data[i] == "$" and data[i - 1] == "$"):
        outputdata = outputdata + data[i]

print (outputdata)

data = outputdata
table = data.split("$")
#print(table)
keyVal = 0


#brute force to remove index 0
i = 1
while i<(len(table)-1):
    if(table[i].isnumeric()):
        keyVal = int(table[i])
        if (not(keyVal in krewes)):
            krewes[keyVal] = []
    else:
        krewes[keyVal].append("name: " + table[i] + "\nduckie: " + table[i+1])
        i+=1
    i+=1
        
a = (random.choice(list(krewes)))
print("period: " + str(a))
b = (random.choice(list(krewes[a])))
print(b)