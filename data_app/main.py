from flask import Flask
from data_app.data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'api_server_test-task'

if __name__ == '__main__':
    db_session.global_init("db/database.db")
    app.run()
