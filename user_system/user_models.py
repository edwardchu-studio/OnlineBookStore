from werkzeug.security import generate_password_hash, check_password_hash
from config import start_database


def buyer_valid_login(username:str, password:str):
    conn = start_database()
    cursor = conn.cursor()
    cursor.execute("SELECT LoginPassword from Buyer where UserName=\'" + username +"\'")
    data = cursor.fetchone()
    if data is not None:
        return True
    return False

def buyer_register(data:[]):
    conn = start_database()
    cursor = conn.cursor()
    username = data['username']
    password = generate_password_hash(data['password'])
    email = data['email']
    insert = "insert into Buyer(BuyerID,LoginPassword,UserName,Email) " \
             + "values(0,\'" + str(password) + "\','" + str(username) + "\'" \
             + ",\'" + str(email) + "\');"
    cursor.execute(insert)
