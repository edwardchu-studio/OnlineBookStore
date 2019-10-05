from __init__ import app
from flask import render_template, request, url_for, redirect, session
from user_system.user_forms import LoginForm
from user_system.user_models import buyer_valid_login


from user_system.user_route import *
from ticket_book.ticket_route import *


@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    loginform = LoginForm()
    querygood = QueryGoodsForm()
    if request.method == "GET":
        literatures = show_good_l(category='literature')
        knowledges = show_good_k(category='knowledge')
        lifes = show_good_li(category='life')
        managements = show_good_m(category='management')
        techs = show_good_t(category='tech')
        wanteds = show_good_w(category='wanteds')
        return render_template("ticket_template/tourist_index.html",logform=loginform, goodform=querygood,literatures=literatures,knowledges=knowledges,lifes=lifes,managements=managements,techs=techs,wanteds=wanteds)
    else:
        if request.form['key'] == "login":
            loginform = LoginForm(formdata=request.form)
            if loginform.validate():
                username = loginform.data['username']
                password = loginform.data['password']
                if buyer_valid_login(username, password):
                    session['username'] = username
                    print("success")
                    return redirect(url_for("buyer_index"))
            else :
                    return render_template('ticket_template/tourist_index.html', logform=loginform, goodform=querygood)

        elif request.form['key'] == 'query':
            querygoodform = QueryGoodsForm(form=request.form)
            loginform = LoginForm()
            if querygoodform.validate():
                bookname = querygoodform.data['bookname']
                query = book_info_query(bookname)
            return render_template('ticket_template/tourist_index.html', title='Home', logform=loginform, goodform=querygoodform,query=query)
        return redirect(url_for("index"))


@app.route('/logout',methods=['POST', "GET"])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run()


