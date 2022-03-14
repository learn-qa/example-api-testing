Feature: Users API
  An API to handle users requests

  Scenario: Able to get all users
    When I make a GET request to url "http://localhost:3000/api/users"
    Then response should have a status 200
    And response data of size 10
    And response data matches the schema users

  Scenario: Able to get a user
    When I make a GET request to url "http://localhost:3000/api/users/222"
    Then response should have a status 200
    And response data matches the schema user

  Scenario: Able to create a user
    When I make a POST request to url "http://localhost:3000/api/users"
    Then response should have a status 201
    And response received with success message
    And response received with userId

  Scenario: Able to update a user
    When I make a PUT request to url "http://localhost:3000/api/users/201"
    Then response should have a status 200
    And response received with success message

  Scenario: Able to delete a user
    When I make a DELETE request to url "http://localhost:3000/api/users/201"
    Then response should have a status 200