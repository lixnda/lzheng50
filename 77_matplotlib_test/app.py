from flask import Flask
from flask import render_template
import sqlite3
import csv
import matplotlib

#used to fix 'NSInternalInconsistencyException' 
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def main():
    DB_FILE="test.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS snake(game INTEGER, length INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS news(show TEXT, nine REAL, ten REAL, eleven REAL)")

    with open('static/snakes_count_1000.csv', mode='r') as file:
        c.execute("DELETE FROM snake")
        data = csv.DictReader(file)
        for row in data:
            game = row['number']
            length = row['length']
            command="INSERT INTO snake VALUES(?, ?)"
            c.execute(command, (game, length))
    db.commit()
    
    with open('static/news_decline.csv', mode='r') as file:
        c.execute("DELETE FROM news")
        data = csv.DictReader(file)
        print("Headers:", data.fieldnames)
        for row in data:
            show = row['show']
            nine = row[' one'] #seems like headers have space in front of them, not sure why
            ten = row[' two']
            eleven = row[' three']
            command = "INSERT INTO news VALUES(?, ?, ?, ?)"
            c.execute(command, (show, nine, ten, eleven))

    db.commit()

    #using pyplot
    plt.figure()
    c.execute("SELECT * from snake")
    a = c.fetchall()
    for row in a:
        x = row[0]
        y = row[1]
        plt.plot(x,y,'ro')
    plt.xlabel("game number")
    plt.ylabel("snake length")

    plt.savefig('static/foo.png')

    #using oo-style. graph has multiple row to display changes in different news stations
    plt.figure()
    c.execute("SELECT * from news")
    b = c.fetchall()
    fig, axs = plt.subplots(6, 1, sharey=True, figsize=(8, 10)) #6 rows by 1 column (each subplot refered to as axs[index])
    num = 0
    for row in b:
        axs[num].plot((2009, 2010, 2011), (row[1], row[2], row[3]), '*-')
        axs[num].set_xlabel(row[0])
        axs[num].set_ylabel("average viewership")
        axs[num].set_xticks([2009, 2010, 2011])
        num+=1
    plt.tight_layout() #adjusts padding

    #usually, plt.show() can be used to display plot, but this function saves it as a png in the static folder
    fig.savefig('static/goo.png')

    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()




