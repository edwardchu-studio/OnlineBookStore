from __init__ import app
from flask import render_template, request, url_for, redirect, session
from ticket_book.ticket_forms import *
from ticket_book.ticket_models import *
from user_system.user_forms import LoginForm
from user_system.user_models import buyer_valid_login

@app.route('/tourist_book_detail/<int:id>', methods=['GET', 'POST'])
def tourist_book_detail(id):
    book = select_good(id)
    bookbuyerid = bookbuyer_id_query(id)
    bookbuyer = buyer_username_query(bookbuyerid)
    if request.method == 'GET':
        loginform = LoginForm()
        form = BuyBookForm()
        return render_template('ticket_template/tourist_book_detail.html',logform=loginform, title='book detail', book=book, form=form, bookbuyer=bookbuyer)
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
                    return redirect(url_for("index"))
        else:
            return redirect(url_for("buyer_index"))


@app.route('/buyer_book_detail/<int:id>', methods=['GET', 'POST'])
def buyer_book_detail(id):
    if 'username' in session:
        bookbuyerid = bookbuyer_id_query(id)
        bookbuyer = buyer_username_query(bookbuyerid)
        book = select_good(id)
        if request.method == 'GET':
            username = session['username']
            form = BuyBookForm()
            return render_template('ticket_template/buyer_book_detail.html',username = username, title='book detail', book=book, form=form, bookbuyer=bookbuyer)
        else:
            form = BuyBookForm(formdata=request.form)
            isSend = form.data['isSend']
            address = form.data['address']
            if isSend == True:
                isSend = '1'
            else:
                isSend = '0'
            # buyer_booking(buyerid:int, sellerid:int, bookid:int, sellprice:decimal, isSend:boolean, address:str):
            buyerid = buyer_id_query(session['username'])
            buyer_booking(buyerid, book[0], book[1], book[6], isSend, address)
            return redirect(url_for("buyer_index"))
    else:
         return redirect(url_for("index"))


@app.route('/buyer_index', methods=['POST', 'GET'])
def buyer_index():
    if 'username' in session:
        if request.method == "GET":
            username = session['username']
            querygood = QueryGoodsForm()
            literatures = show_good_l(category='literature')
            knowledges = show_good_k(category='knowledge')
            lifes = show_good_li(category='life')
            managements = show_good_m(category='management')
            techs = show_good_t(category='tech')
            wanteds = show_good_w(category='wanted')
            return render_template("ticket_template/buyer_index.html", username = username , goodform=querygood,literatures=literatures,knowledges=knowledges,lifes=lifes,managements=managements,techs=techs, wanteds=wanteds)
        else:
            form = QueryGoodsForm(formdata=request.form)
            if form.validate():
                bookname = form.data['bookname']
                query = book_info_query(bookname)
                return render_template('ticket_template/buyer_index.html', title='Home', form=form, query=query)
    else:
        return redirect(url_for("index"))


@app.route('/buyer_add', methods=['GET', 'POST'])
def buyer_add():
    user = session['username']
    if request.method == 'GET':
        form = buyerAdd()
        return render_template('ticket_template/buyer_add.html', title='buyer add', form=form, user=user)
    else:
        form = buyerAdd(formdata=request.form)
        bookname = form.data['bookname']
        isbn = form.data['isbn']
        category = form.data['category']
        price = form.data['price']
        sellprice = form.data['sellprice']
        content = form.data['content']
        buyerid = buyer_id_query(session['username'])
        wanted = form.data['wanted']
        image = form.data['image']
        if wanted == True:
                wanted = '1'
        else:
                wanted = '0'
        buyer_add_book(buyerid,bookname,isbn,category,price,sellprice,content,wanted,image)
        return redirect('/buyer_listofgoods')
       
    


@app.route('/buyer_edit/<int:id>', methods=['POST', 'GET'])
def buyer_edit_good(id):
    good = select_good(id)
    user = session['username']
    if request.method == 'GET':
        form = buyerAdd()
        return render_template('ticket_template/buyer_edit.html', title='buyer edit', good=good,user=user, form=form)
    else:
        bookid = id
        form = buyerAdd(formdata=request.form)
        bookname = form.data['bookname']
        isbn = form.data['isbn']
        category = form.data['category']
        price = form.data['price']
        sellprice = form.data['sellprice']
        content = form.data['content']
        buyerid = buyer_id_query(session['username'])
        wanted = form.data['wanted']
        image = form.data['image']
        if wanted == True:
                wanted = '1'
        else:
                wanted = '0'
        buyer_edit_book(bookid,buyerid,bookname,isbn,category,price,sellprice,content,wanted,image)
        good = select_good(id)
        return redirect(url_for("buyer_listofgoods"))


@app.route('/buyer_listofgoods', methods=['GET', 'POST'])
def buyer_listofgoods():
    if 'username' in session:
        user = session['username']
        if request.method == 'GET':
            buyer_id = buyer_id_query(session['username'])
            seelist = buyer_seelist(buyer_id)
            return render_template('ticket_template/buyer_listofgoods.html', title='list of books', user=user, seelist=seelist)
        else:
            buyer_id = buyer_id_query(session['username'])
            seelist = buyer_seelist(buyer_id)
            return render_template('ticket_template/buyer_listofgoods.html', title='list of books', user=user, seelist=seelist)
    return render_template('ticket_template/buyer_listofgoods.html', title='list of books', user=user, seelist=seelist)

