#Linda Zheng
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
c.execute("CREATE TABLE roster (name TEXT, age INTERGER, id INTEGER)")
c.execute("CREATE TABLE course (code TEXT, mark INTERGER, id INTEGER)")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

file = open('students.csv', mode='r', newline='')
csv_reader = csv.DictReader(file) #reads csv file as an ordered dictionary
for row in csv_reader:
    #print(row)
    name = (row['name'])
    age = (row['age'])
    ids = (row['id'])
    command = "INSERT INTO roster VALUES (?, ?, ?)" #the ? denotate that it should take the valuable of variables in previous lines
    c.execute(command, (name, age, ids))    # run SQL statement (also ensures it knows what values previous parameters refering to?)
    

file = open('courses.csv', mode='r', newline='')
csv_reader = csv.DictReader(file) #reads csv file as an ordered dictionary
for row in csv_reader:
    code = (row['code'])
    mark = (row['mark'])
    ids = (row['id'])
    command = "INSERT INTO course VALUES (?, ?, ?)"
    c.execute(command, (code, mark, ids))
#==========================================================


#this doesn't print anything. is it suppose to? how do we know the database worked?
#c.execute("SELECT * FROM roster")

db.commit() #save changes


db.close()  #close database
