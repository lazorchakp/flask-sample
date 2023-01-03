from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello New World"
    return name

if __name__ == "__main__":
    app.run(debug=True)
