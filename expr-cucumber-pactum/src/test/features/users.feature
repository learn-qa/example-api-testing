Feature: Users

    Able to manage Users

    Scenario: Able to get all users
        Given I make a GET request to url "http://127.0.0.1:3000/api/users"
        When I receive a response
        Then response should have a status 200
        And response data of size 10
        And response data of type array
        And response data at index 0 matches schema

    Scenario: Able to get a user
        Given I make a GET request to url "http://127.0.0.1:3000/api/users/200"
        When I receive a response
        Then response should have a status 200
        And response data matches schema