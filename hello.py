from flask import Flask,make_response,redirect,abort
from flask.ext.script import Manager
from flask import render_template

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cookie')
def cookie():
    response = make_response('<h1>This docment carries a cookie!</h1>')
    response.set_cookie('answer','mmx')
    return response

@app.route('/url/<url>')
def url(url):
    return redirect(url)

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

@app.route('/login/<name>')
def user(name):
    return render_template('user.html', username = name)

if __name__ == '__main__':
#    app.run(debug = True)
    manager.run()
