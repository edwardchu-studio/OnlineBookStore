from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'fbaubfaibiuab21312/f'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Vlifestyle'
app.config['MYSQL_DATABASE_DB'] = 'BookOnline'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
