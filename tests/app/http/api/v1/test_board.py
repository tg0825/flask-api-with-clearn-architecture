import json


# def test_get_board(client):
#     board = False
#     assert board, '게시글이 없습니다.'


def test_create_board(client):
    data = {
        "title": "123",
        "body": "123"
    }
    response = client.post('/api/board', json=data)
    board = False
    assert response.status_code == 200, 'api 실패'
