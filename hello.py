from flask import Flask,make_response,redirect,abort
from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap
    
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

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

@app.route('/404')
def show_404():
    return render_template('404.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
#    app.run(debug = True)
    manager.run()
