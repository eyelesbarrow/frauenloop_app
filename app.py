import sys, os
from flask import Flask


app = Flask(__name__)# URL Routing — Home Page

@app.route('/')
def index():
    return "Sample Static App!"

if __name__ == '__main__':
    # Set the environment variable for Flask
    os.environ['FLASK_APP'] = 'app.py'
    
    # Run the Flask application
    app.run(port=8000)


            
