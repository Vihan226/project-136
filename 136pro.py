from flask import Flask, jsonify, request

app= Flask(__name__)
@app.route("/")

def index():
    return 'index';

@app.route("/planet")
def planet():
    


if __name__== '__main__':
    app.run()
