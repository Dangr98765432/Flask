from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    first_name = '<h1>John</h1>'

    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template(
        "index.html",
        first_name=first_name,
        favorite_pizza=favorite_pizza
    )


@app.route('/user/<user_name>')
def user(user_name):
    return render_template(
        template_name_or_list="user.html",
        user_name=user_name,
    )


if __name__ == '__main__':
    app.run(
        debug=True,
        use_reloader=False,
        port=5001,
    )

