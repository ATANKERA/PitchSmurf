from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretHere'


class AnotherForm(FlaskForm):
    company = StringField('Company Name : ')


#Works!
@app.route('/')
def default():
    return "failed"


#Works!
@app.route('/helloworld')
def hello_world():
   return render_template("index.html")



@app.route('/form', methods=['GET', 'POST'])
def form3():
    form3 = AnotherForm()
    if form3.validate_on_submit():
        if form3.company.data == "":
            return redirect(url_for('f404'))
        return redirect(url_for('fcomp',companyname = form3.company.data))
    return render_template('form3.html', form=form3)



@app.route('/company/<path:companyname>')
def fcomp(companyname):
    return companyname


@app.route('/404')
def f404():
    return render_template('404page.html')




if __name__ == '__main__':
    app.run(debug=True)
