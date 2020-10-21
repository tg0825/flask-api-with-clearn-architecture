class LocalConfig:
    DEBUG = True
    SERVICE_NAME = "board"

    db = {
        "user": "root",
        "password": "qwert",
        "host": "127.0.0.1",
        "port": "3306",
        "database": "flask_test",
    }

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"


config = {"default": LocalConfig}
