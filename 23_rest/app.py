"""
Linda Zheng, Nia Lam
teamname
SoftDev
K23 - rest api
2024-11-20
time spent: 1

DISCO:
with request.urlopen you need to decrypt the byte format of the reaf function
into a json formatted string
with request.get you can directly use the function .json to convert into a dict
"""

from flask import Flask, render_template
import urllib.request
import requests
import json

app = Flask(__name__)

@app.route("/")
def main():
    with open("key_nasa.txt") as file:
        api_key = file.read()
    """
    with urllib.request.urlopen(f"https://api.nasa.gov/planetary/apod?api_key={api_key}") as response:
        html = response.read()
        nasa = json.loads(html.decode())
    copy = nasa["copyright"]
    date = nasa["date"]
    explain = nasa["explanation"]
    img = nasa["url"]
    title = nasa["title"]
    """
        
    with requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}") as response:
        nasa = response.json()
    copy = nasa["copyright"]
    date = nasa["date"]
    explain = nasa["explanation"]
    img = nasa["url"]
    title = nasa["title"]
    """    
    #html is printed as a byte
    print(html)
    print(nasa)
    """
        
    return(render_template("main.html", title=title, img_url=img, description=explain, date=date ))

if __name__ == "__main__":
    app.debug = True
    app.run()

