from __init__ import app
from user_system.user_models import *
from user_system.user_forms import *
from flask import flash, render_template, request, url_for, redirect, session

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        form_register = RegistrationForm()
        return render_template('user_template/register.html', form_register=form_register)
    else:
        form_register = RegistrationForm(formdata=request.form)
        if form_register.validate():
            buyer_register(form_register.data)
            flash(u"Registration Success")
            return redirect(url_for('index'))
        else:
           return render_template('user_template/register.html', form_register=form_register)