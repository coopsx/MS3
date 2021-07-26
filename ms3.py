from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'name': 'Tom Jackson',
        'title': 'Introduction',
        'content': 'Introductory Post',
        'date': '26 JUNE, 2021'
    },
    {
        'name': 'James Cooper',
        'title': 'Barolo',
        'content': 'Barolo Wine Review',
        'date': '28 JUNE, 2021'
    }
]


@app.route("/")
@app.route("/index")
def hello_world():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/blog")
def blog():
    return render_template('blog.html', title='Blog', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
