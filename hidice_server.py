#!/usr/bin/env python3
# 
from flask import *

app = Flask(__name__)

class State:
    def __init__(self):
        self.bumped = 0

    def bump(self):
        self.bumped += 1
        return self.bumped
    
    def bumps(self) -> int:
        return self.bumped


state = State()

@app.route("/", methods=["GET"])
def main():
    return render_template("main.html")

@app.route("/bump", methods=["POST"])
def bump():
    print("Bump!")
    state.bump()
    return f"bumps thus far: {state.bumps()}"


app.run()