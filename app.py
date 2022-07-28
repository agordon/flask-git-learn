from flask import Flask,render_template,request
from flask_wtf import FlaskForm ## NEW
from wtforms import StringField,IntegerField, SubmitField ## NEW
from wtforms.validators import DataRequired,NumberRange ## NEW
from flask_bootstrap import Bootstrap
from pprint import pprint

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False
b = Bootstrap(app)

@app.route("/")
def boots1():
    return render_template("boots1.html")

@app.route("/boots2")
def boots2():
    return render_template("boots2.html")

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(13,115)])
    number = IntegerField('Choose a number:')
    go = SubmitField()

@app.route("/form-test",methods=["GET","POST"])
def form_test():
    form = MyForm()
    if form.is_submitted():
        print("User submitted the form, validating input now...")
        if form.validate_on_submit():
            print("Form OK")
        else:
            print("Form Error:")
            pprint(form.errors)
    else:
        print("User is viewing the form")

    return render_template("form_test.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
