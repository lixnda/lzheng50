"""
Linda Zheng
SoftDev
K09 -- Reading CSV Files
2024-09-19
time spent: 
"""

from flask import Flask
import random

app = Flask(__name__)


def randO(types):
    file = open("occupations.csv")

    data = file.read().strip().split("\n")


    occupation = {}
    weight = []

    for i in range(1, len(data)-1):
        job = data[i]
        if job[0]=='"':
            key = job[1:].index('"')
            
            #replacing necessary comma with placeholder
            temp = job[0:key].replace(",","<>") + job[key:]
            data[i] = temp


    for i in range(1, len(data)-1):
        splitted = data[i].split(",")
        
        #replacing placeholder with comma
        splitted[0] = splitted[0].replace("<>", ",")
        occupation[splitted[0]] = splitted[1]
        weight.append(float(splitted[1]))

     
    randO = random.choices(list(occupation), weights=weight, k=1)
    
    if(types==1):
        return(randO)
    else:
        return(occupation)

def table():
    occupation = (randO(2))
    output = "<table><tr><th>Job Class</th><th>Percentage></th><tr>"
    for i in occupation:
        output=output+"<tr><td>"+i+"</td><td>"+occupation[i]+"</td></tr>"
    output=output + "</table>"
    return output
    

@app.route("/")
def hello_world():
    print(__name__)
    return(f"<h1>TeamName: Linda, Amanda, Andy</h1><hr>Your desiny is: {randO(1)} \n {table()}")

app.run()