import pytest
import requests
from jsonschema.validators import validate
from pytest_bdd import when, parsers, then, scenarios

from UsersHelper import UsersHelper

users_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",

    "type": "array",
    "properties": {
        "data": {
            "type": "object"
        }
    }
}

user_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",

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

payload = {
    "firstName": "Francis",
    "lastName": "Chelladurai",
    "address": "7, hgdjgtuy, jhj, jhghg",
    "phone": "0788765545",
    "email": "gfgfgf@test.com"
}


@pytest.fixture
def application():
    helper = UsersHelper()
    return helper


scenarios('../features/users.feature')


@when(parsers.parse('I make a {method} request to url "{url}"'))
def get_request_when(application, method, url):
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, payload)
    elif method == 'PUT':
        response = requests.put(url, payload)
    else:
        response = requests.delete(url)

    resp_body = response.json()
    application.status_code = response.status_code
    if 'data' in resp_body:
        application.users = resp_body["data"]
        application.user = resp_body["data"][0]
    else:
        application.response = resp_body


@then(parsers.parse('response should have a status {resp_code}'))
def check_status_code(application, resp_code):
    assert application.status_code == int(resp_code)


@then(parsers.parse('response data of size {size:d}'))
def check_status_code(application, size):
    assert len(application.users) == size


@then('response data matches the schema users')
def check_status_code(application):
    validate(instance=application.users, schema=users_schema)


@then('response data matches the schema user')
def check_status_code(application):
    assert application.response['userId'] == 222
    validate(instance=application.response, schema=user_schema)


@then('response received with userId')
def check_response_for_userid(application):
    assert isinstance(application.response['userId'], int)


@then('response received with success message')
def check_response_for_userid(application):
    assert application.response['status'] == 'success'
# def test_user_create_check():
#     payload = {
#         "firstName": "Francis",
#         "lastName": "Chelladurai",
#         "address": "7, hgdjgtuy, jhj, jhghg",
#         "phone": "0788765545",
#         "email": "gfgfgf@test.com"
#     }
#     response = requests.post(url="http://localhost:3000/api/users", data=payload)
#     assert response.status_code == 201
#     resp_body = response.json()
#
#     assert resp_body["status"] == "success"
#     assert type(resp_body["userId"]) == int
#
#
# def test_user_update_check():
#     payload = {
#         "firstName": "Francis",
#         "lastName": "Chelladurai",
#         "address": "7, hgdjgtuy, jhj, jhghg",
#         "phone": "0788765545",
#         "email": "gfgfgf@test.com"
#     }
#     response = requests.put("http://localhost:3000/api/users/200")
#     assert response.status_code == 200
#
#     resp_body = response.json()
#     assert resp_body["status"] == "success"
#
#
# def test_user_delete_check():
#     response = requests.delete("http://localhost:3000/api/users/200")
#     assert response.status_code == 200
#
#     resp_body = response.json()
#     assert resp_body["status"] == "success"
