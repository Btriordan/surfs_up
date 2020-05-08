from flask import Flask

# Creates a new Flask - or online database
app = Flask(__name__)

# Define starting point to make our first route
# @app.route('/')

@app.route("/")
def index():
    return "Hello, world!"