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
# from flask import Flask , render_template
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from datetime import datetime

# app = Flask(__name__)
# bootstrap = Bootstrap(app)
# moment = Moment(app)

# @app.route('/')
# def index():
#  return render_template('index.html',
#  current_time=datetime.utcnow())

# app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)

# @app.errorhandler(404)
# def page_not_found(e):
#  return render_template('404.html'), 404
# @app.errorhandler(500)
# def internal_server_error(e):
#  return render_template('500.html'), 500

# if __name__ == '__main__':
#     app.run(debug=True)


#Activity 1.4
from flask import Flask , render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkeythatisveryhardtoguessandchangeforhackers'
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameEmailForm(FlaskForm):
 name = StringField('What is your name?', validators=[DataRequired()])
 email = StringField('What is your UofT Email address?', validators=[DataRequired(), Email()])
 submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    flag = False
    form = NameEmailForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != name:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != email:
            flash('Looks like you have changed your email!')


        if email.endswith("utoronto.ca"):
            flag = True
            session['email'] = email
        else:
            flag = False
            session['email'] = None

        session['name'] = name
        return redirect(url_for('index', name=name, email=email))
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>')
def user(name):
        email = session.get('email')
        return render_template('user.html', name=name, email=email)


if __name__ == '__main__':
    app.run(debug=True)






