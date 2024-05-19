# # Static flask
# # get from http://127.0.0.1:8000/

# from flask import Flask

# app = Flask(__name__)
# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'
# if __name__ == '__main__':
#     app.run(debug=True)

# # dynammic flask
# # get from http://127.0.0.1:8000/index/ahmed

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'
# @app.route('/index/<name>')
# def hello(name):
#     return '<h1>Hello, %s!</h1>' % name
# if __name__ == '__main__':
#     app.run(debug=True)

# # use Templetes

# from flask import Flask, render_template
# app = Flask(__name__)
 
# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'
 
# @app.route('/index/<name>')
# def hello(name):
#     return render_template('index.html', name = name)
 
# if __name__ == '__main__':
#     app.run(debug = True)

# # Use Design With Dynamic
# from flask import Flask, render_template
# from flask_bootstrap import Bootstrap  # Correct import statement for Flask-Bootstrap

# app = Flask(__name__)
# bootstrap = Bootstrap(app)

# # Your routes and other application logic here...

# @app.route('/index/<name>')
# def hello(name):
#     return render_template('index2.html', name=name)

# if __name__ == '__main__':
#     app.run(debug=True)

# # FORMS
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
 
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
 
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index3.html', form = form, name = name )
