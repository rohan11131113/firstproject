# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I am Rohan – DevOps Intern Ready!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
