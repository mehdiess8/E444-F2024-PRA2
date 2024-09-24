#Activity 1.2.1
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#  return '<h1>Hello World!</h1>'


#Activity 1.2.2
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#  return '<h1>Hello World!</h1>'
# @app.route('/user/<name>')
# def user(name):
#  return '<h1>Hello, {}!</h1>'.format(name)


#Activity 1.3
from flask import Flask , render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
 return render_template('index.html',
 current_time=datetime.utcnow())

app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)


#Activity 1.4
# from flask import Flask, render_template, session, redirect, url_for, flash
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from datetime import datetime, timezone
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

# class NameForm(FlaskForm):
#     name = StringField('What is your name?', validators=[DataRequired()])
#     submit = SubmitField('Submit')





