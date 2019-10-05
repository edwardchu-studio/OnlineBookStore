from config import start_database

from werkzeug.utils import secure_filename
import time
import os
import cv2
import time 
import datetime


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])


def book_info_query(bookname: str) -> []:
    conn = start_database()
    cursor = conn.cursor()
    insert = "select * from Book where Bookname LIKE \'" + bookname + "%\';"
    cursor.execute(insert)
    data = cursor.fetchall()
    if data:
        return data


def buyer_booking(buyerid: int, sellerid: int, bookid: int, sellprice: float, isSend: int, Address: str):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    # timestamp = Date + Time
    conn = start_database()
    cursor = conn.cursor()
    # cursor = start_database()
    insert = """

INSERT INTO
  `Order` (
    `BuyerID`,
    `SellerID`,
    `BookID`,
    `OrderTime`,
    `SellPrice`,
    `isSend`,
    `Address`
  )
VALUES
  (
    %d,
    %d,
    %d,
    NOW(),
    %f,
    %s,
    '%s'
  );
    """ % (buyerid, sellerid, bookid, sellprice, isSend, Address)
    print(insert)
    cursor.execute(insert)
    # cursor.execute("INSERT into Order values ( ,"+buyerid+","+buyerid+","+bookname+",0,"+timestamp+", NULL, NULL, NULL, NULL,"+amount+")")
    data = cursor.fetchone()


def buyer_add_book(buyerid: int, bookname: str, isbn: str , category: str, price: str, sellprice: str, content: str, wanted: str, image: str):
    conn = start_database()
    cursor = conn.cursor()
    insert = "insert into `Book` values("+str(buyerid)+",null, \'" \
             + bookname + "\',\'" + isbn + "\',\'" + category + "\'," + str(price) + "," + str(sellprice) + ",\'" + str(
        content) + "\',\'"+wanted+"\',\'"+image+"\');"
    print(insert)
    cursor.execute(insert)
    data = cursor.fetchone()

def buyer_edit_book(bookid:int, buyerid: int, bookname: str, isbn: str , category: str, price: str, sellprice: str, content: str, wanted: str, image: str):
    conn = start_database()
    cursor = conn.cursor()
    insert = """

    UPDATE Book SET  
    bookname = '%s',
    isbn = '%s',
    category = '%s',
    price = %s,
    sellprice = %s,
    content = '%s',
    wanted = %s,
    imageURL = '%s'
    WHERE SellerID = %d AND BookID = %d
    ;
        """ % (bookname, isbn, category, price, sellprice, content, wanted, image, buyerid,bookid)
    # insert = "UPDATE `Book` set `bookname` = \'" + bookname + "\', `isbn`=\'" \
    #          + isbn + "\', `category`=\'" + category + "\', `price`=\'" + price + "\', `SellPrice`=" + sellprice + "\', `content`="+ content" where `BoodID`=" + str(BookID) + ";"
    print(insert)
    cursor.execute(insert)
    data = cursor.fetchone()

def show_good(start_limit=0, end_limit=100):
    conn = start_database()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Book WHERE Category = 'literature' LIMIT {start_limit},{end_limit};")
    data = cursor.fetchall()
    if data:
        return data
    else:
        return []

def show_good_l(category='literature', start_limit=0, end_limit=100):
    conn = start_database()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Book WHERE Category = 'literature' LIMIT {start_limit},{end_limit};")
    data = cursor.fetchall()
    if data:
        return data
    else:
        return []

def show_good_k(category='knowledge', start_limit=0, end_limit=100):
    conn = start_database()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Book WHERE Category = 'knowledge' LIMIT {start_limit},{end_limit};")
    data = cursor.fetchall()
    if data:
        return data
    else:
        return []

def show_good_li(category='life', start_limit=0, end_limit=100):
    conn = start_database()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Book WHERE Category = 'life' LIMIT {start_limit},{end_limit};")
    data = cursor.fetchall()
    if data:
        return data
    else:
        return []

def show_good_t(category='tech', start_limit=0, end_limit=100):
    conn = start_database()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Book WHERE Category = 'tech' LIMIT {start_limit},{end_limit};")
    data = cursor.fetchall()
    if data:
        return data
    else:
        return []

def show_good_m(category='management', start_limit=0, end_limit=100):
    conn = start_database()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Book WHERE Category = 'management' LIMIT {start_limit},{end_limit};")
    data = cursor.fetchall()
    if data:
        return data
    else:
        return []

def show_good_w(category='wanted', start_limit=0, end_limit=100):
    conn = start_database()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Book WHERE Wanted = 1 LIMIT {start_limit},{end_limit};")
    data = cursor.fetchall()
    if data:
        return data
    else:
        return []

def select_good(book_id):
    conn = start_database()
    cursor = conn.cursor()
    insert = f"SELECT * FROM Book WHERE BookID={book_id}"
    print(insert)
    cursor.execute(insert)
    data = cursor.fetchall()
    if data:
        return data[0]


def buyer_seelist(buyerid: int):
    conn = start_database()
    cursor = conn.cursor()
    insert = "select * from `Book` where SellerID = " + str(buyerid) + ";"
    print(insert)
    cursor.execute(insert)
    data = cursor.fetchall()
    if data:
        return data

def buyer_id_query(username: str):
    conn = start_database()
    cursor = conn.cursor()
    insert = "select BuyerID from Buyer where UserName = \'" + username + "\';"
    cursor.execute(insert)
    return cursor.fetchone()[0]

def bookbuyer_id_query(bookid: int):
    conn = start_database()
    cursor = conn.cursor()
    insert = "select SellerID from Book where BookID = \'" + str(bookid) + "\';"
    cursor.execute(insert)
    return cursor.fetchone()[0]

def buyer_username_query(buyerid: int):
    conn = start_database()
    cursor = conn.cursor()
    insert = "select UserName from Buyer where BuyerID = \'" + str(buyerid) + "\';"
    cursor.execute(insert)
    return cursor.fetchone()[0]

# def buyer_id_query(username: str):
#     conn = start_database()
#     cursor = conn.cursor()
#     insert = "select BuyerId from Buyer where UserName = \'" + username + "\';"
#     cursor.execute(insert)
#     return cursor.fetchone()[0]
