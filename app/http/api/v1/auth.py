from app.http.api import api


@api.route("/auth/login", methods=["GET"])
def login():
    pass
