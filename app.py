from flask import Flask, render_template
import json
import os
import random

app = Flask(__name__)

# Load random puzzle in folder from JSON file 
pathToPuzzles = os.path.join(os.getcwd(), 'puzzles')
""" randomPuzzle = random.choice(os.listdir(pathToPuzzles)) """
filePath = os.path.join(pathToPuzzles, "2_30x30.json")

with open(filePath, "r") as file:
    puzzle = json.load(file)
    

@app.route('/')
def index():
    return render_template('table.html', columns=puzzle['columnNumbers'], rows=puzzle['rowNumbers'])
