"""
Linda Zheng
Boas
SoftDev
K<18> -- serving queen CCSstuyle
2024-10-26
time spent:
"""
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

app.run();
