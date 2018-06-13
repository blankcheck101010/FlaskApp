from flask import Flask, render_template, url_for
app = Flask(__name__)  # this is the name of the module


posts = [
    {
        'author': 'Saul Alvarez',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Maria Alvarez',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


# '/' the root(home) page of website
# decorators add additional functionality to existing
# functions


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def hello():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
