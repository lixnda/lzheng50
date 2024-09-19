"""
Linda Zheng
Boas
SoftDev
K<06> -- CSV files
2024-09-18
time spent: 

"""

import random

file = open("occupations.csv")

data = file.read().strip().split("\n")


occupation = {}

for i in range(1, len(data)-1):
    job = data[i]
    if job[0]=='"':
        key = job[1:].index('"')
        temp = job[0:key].replace(",","<>") + job[key:]
        data[i] = temp

for i in range(1, len(data)-1):
    splitted = data[i].split(",")
    print (splitted)
    splitted[0].replace("<>", ",")
    occupation[splitted[0]] = splitted[1]