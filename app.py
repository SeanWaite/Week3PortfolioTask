from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def easyDoesIt():

    user = 'Sean'
    title = 'Drink'
    drinks = [
        {'Water':'https://en.wikipedia.org/wiki/Water'},
        {'Green Tea':'https://en.wikipedia.org/wiki/Green_tea'},
        {'Beer':'https://en.wikipedia.org/wiki/Beer'},
        {'Whisky':'https://en.wikipedia.org/wiki/Whisky'}
        ]

    return render_template("index.html", title=title, user=user, drinks=drinks)
    #return "<h1>Easy does it!</h1>"

if __name__ == '__main__':
    app.run()
