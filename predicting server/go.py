from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
import forDeploy
#nltk.data.path.append('./nltk_data/')

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    # form = ReusableForm(request.form)
    # print(form.errors)
    if request.method == 'POST':
        print("--------!!----------")
        print(request.data)
        print("--------------------")
        data = json.loads(request.data)
        name = data['name']
        pr = forDeploy.predict(name)
        # exec(open("predict.py").read())
        js = {'name': pr}
        # if form.validate():
            # Save the comment here.
            #flash('Hello ' + name)
            
        return json.dumps(js)
        # return json.dumps(js);
        # else:
            # flash('All the form fields are required. ')
    return json.dumps('{"name":"kai"}');



if __name__ == "__main__":
    app.run()


