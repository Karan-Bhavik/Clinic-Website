# Flask application with clinic website routes

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Clinic Website!'

if __name__ == '__main__':
    app.run(debug=True)