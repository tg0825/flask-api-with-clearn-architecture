from flask import request

from app.http.api import api
from app.http.requests.board.create_board import CreateBoardRequestObject

@api.route("/board")
def get_board():
    return "get board"


@api.route("/board", methods=["POST"])
def create_board():
    # 1. request 데이터를 파싱
    req = CreateBoardRequestObject.from_dict(a_dict=request.json)
    # 2. 유즈케이스 실행 (dto)
    # 3. 프리젠터 실행
    return req


@api.route("/board", methods=["DELETE"])
def delete_board():
    return "delete board"
