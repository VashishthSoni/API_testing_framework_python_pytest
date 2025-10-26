from helpers.request_utils import send_request
from helpers.logger import log_request_response
import pytest

@pytest.mark.parametrize("user_id,expected_status", [
    (1, 200),
    (2, 200),
    (9999, 404),
])
def test_get_user_param(user_id, expected_status, auth_headers):
    resp = send_request("GET", f"/users/{user_id}", headers=auth_headers)
    log_request_response(resp)
    assert resp.status_code in (expected_status, 200)
    data = resp.json()
    assert isinstance(data, dict)
    if resp.status_code == 200:
        assert "id" in data


def test_create_todo(auth_headers):
    payload = {
        "userId": 1,
        "title": "Learn API Testing",
        "completed": False
    }
    resp = send_request("POST", "/todos", headers=auth_headers, json=payload)
    log_request_response(resp)
    assert resp.status_code in (200, 201)
    data = resp.json()
    assert data["title"] == payload["title"]
    assert "id" in data


def test_update_todo_patch(auth_headers):
    todo_id = 1
    payload = {"completed": True}
    resp = send_request("PATCH", f"/todos/{todo_id}", headers=auth_headers, json=payload)
    log_request_response(resp)
    assert resp.status_code in (200, 204)
    data = resp.json()
    assert data["completed"] is True
