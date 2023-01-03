from flask import Flask
from contrast.flask import ContrastMiddleware

app = Flask(__name__)
app.wsgi_app = ContrastMiddleware(app)

@app.route('/')
def hello():
    name = "Hello New World with Contrast"
    return name

if __name__ == "__main__":
    app.run(debug=True, port=8000)
