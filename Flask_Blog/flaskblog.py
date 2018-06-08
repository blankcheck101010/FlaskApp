from flask import Flask
app = Flask(__name__)  # this is the name of the module

# '/' the root(home) page of website
# decorators add additional functionality to existing
# functions


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def hello():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
