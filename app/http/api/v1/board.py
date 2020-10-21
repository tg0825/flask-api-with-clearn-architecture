from app.http.api import api


@api.route("/board")
def get_board():
    return "get board"
