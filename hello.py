from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "super secret key"

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a route decorator
@app.route('/')
def index():
    first_name = 'John'
    stuff = 'This is bold text'
    favorite_pizza = ['Pepperoni', 'Cheese', 'Mushrooms', 41]
    return render_template('index.html', first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
        flash('Form Submitted Successfully')
    return render_template('name.html', name=name, form=form)


# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
