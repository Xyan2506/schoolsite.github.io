from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/soul')
def soul():
    return render_template("soul.html")


@app.route('/coolstuff')
def coolstuff():
    return render_template("coolstuff.html")

@app.route('/randomfeature')
def randomfeature():
    return render_template("randomfeature.html")

@app.route('/teamfeature')
def teamfeature():
    return render_template("teamfeature.html")

@app.route('/stufffordevelopers')
def stufffordevelopers():
    return render_template("stufffordevelopers.html")

@app.route('/anotherone')
def anotherone():
    return render_template("anotherone.html")

@app.route('/lasttime')
def lasttime():
    return render_template("lasttime.html")

@app.route('/resourse')
def resourse():
    return render_template("resourse.html")

@app.route('/resoursename')
def resoursename():
    return render_template("resoursename.html")

@app.route('/anotherresourse')
def anotherresourse():
    return render_template("anotherresourse.html")

@app.route('/finalresourse')
def finalresourse():
    return render_template("finalresourse.html")


@app.route('/home/<string:name>/<int:id>')
def name_id(name, id):
    return "User page:" + name + str(id)
if __name__ == "__main__":
    app.run(debug=True)

