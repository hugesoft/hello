from flask import Flask,make_response,redirect,abort
from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.debug = True
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        return render_template('index.html', form=form, name=name)
#        return render_template('index.html')
"""
@app.route('/cookie')
def cookie():
    response = make_response('<h1>This docment carries a cookie!</h1>')
    response.set_cookie('answer','mmx')
    return response
"""

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
#    app.run(debug = True)
    manager.run()
