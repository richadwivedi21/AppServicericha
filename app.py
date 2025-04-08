from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Welcome to Azure Capstone Project. ~Aditya Sharma"

if __name__ == '__main__':
    app.run(debug=True)
