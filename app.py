from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/user/<name>')
def user(name):
    return f"Hello {name}"


if __name__ == '__main__':
    app.run(
        debug=True,
        use_reloader=False,
        port=5001,
    )

