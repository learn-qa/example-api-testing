import requests
from jsonschema import validate

users_schema = {
    "$schema": "https://json-schema.org/schema#",

    "type": "object",
    "properties": {
        "data": {
            "type": "array"
        }
    }
}

user_schema = {
    "$schema": "https://json-schema.org/schema#",

    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "address": {"type": "string"},
        "email": {"type": "string"},
        "phone": {"type": "string"}
    }
}


def test_users_details_check():
    response = requests.get("http://localhost:3000/api/users")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    resp_body = response.json()
    data = resp_body["data"]

    assert len(data) == 10
    validate(instance=resp_body, schema=users_schema)
    validate(instance=data[0], schema=user_schema)


def test_user_details_check():
    response = requests.get("http://localhost:3000/api/users/200")
    assert response.status_code == 200
    resp_body = response.json()

    assert resp_body["userId"] == 200
    validate(instance=resp_body, schema=user_schema)


def test_user_create_check():
    payload = {
        "firstName": "Francis",
        "lastName": "Chelladurai",
        "address": "7, hgdjgtuy, jhj, jhghg",
        "phone": "0788765545",
        "email": "gfgfgf@test.com"
    }
    response = requests.post(url="http://localhost:3000/api/users", data=payload)
    assert response.status_code == 201
    resp_body = response.json()

    assert resp_body["status"] == "success"
    assert type(resp_body["userId"]) == int


def test_user_update_check():
    payload = {
        "firstName": "Francis",
        "lastName": "Chelladurai",
        "address": "7, hgdjgtuy, jhj, jhghg",
        "phone": "0788765545",
        "email": "gfgfgf@test.com"
    }
    response = requests.put("http://localhost:3000/api/users/200")
    assert response.status_code == 200

    resp_body = response.json()
    assert resp_body["status"] == "success"


def test_user_delete_check():
    response = requests.delete("http://localhost:3000/api/users/200")
    assert response.status_code == 200

    resp_body = response.json()
    assert resp_body["status"] == "success"
