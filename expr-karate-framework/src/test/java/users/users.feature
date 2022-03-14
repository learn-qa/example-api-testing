Feature: Able to manage users

  Background:
    * url 'http://localhost:3001/api'

  Scenario: Able to get all users
    Given path '/users'
    When method get
    Then status 200
    And def data = response.data
    And match data == '#[10]'
    And def first = data[0]
    And match first ==
    """
    {
      "firstName": '#string? _.length > 0',
      "lastName": '#string? _.length > 0',
      "address": '#string? _.length > 0',
      "email": '#string? _.length > 0',
      "phone": '#string? _.length > 0',
      "userId": '#number? _ > 0'
    }
    """

  Scenario Outline: Able to get a user
    Given path '/users', <userId>
    When method get
    Then status 200
    And match response ==
    """
    {
      "firstName": '#string? _.length > 0',
      "lastName": '#string? _.length > 0',
      "address": '#string? _.length > 0',
      "email": '#string? _.length > 0',
      "phone": '#string? _.length > 0',
      "userId": <userId>
    }
    """
    Examples:
      | userId |
      | 200    |
      | 333    |

  Scenario: Able to create a user
    Given path '/users'
    And request
      """
      {
        'firstName': 'Francis',
        'lastName': 'Chelladurai',
        'email': 'hguyterugh@test.com',
        'phone': '0896876223',
        'address': '7 hello street, Hello, CT71, US'
      }
      """
    And header Accept = 'application/json'
    When method post
    Then status 201
    And match response ==
      """
      {
        "status": "success",
        "userId": '#number? _ > 0'
      }
      """

  Scenario: Able to update a user
    Given path '/users', 200
    And request
      """
      {
        'firstName': 'Francis',
        'lastName': 'Chelladurai',
        'email': 'hguyterugh@test.com',
        'phone': '0896876223',
        'address': '7 hello street, Hello, CT71, US'
      }
      """
    And header Accept = 'application/json'
    When method put
    Then status 200
    And match response ==
      """
      {
        "status": "success"
      }
      """

  Scenario: Able to delete a user
    Given path '/users', 200
    When method delete
    Then status 200
    And match response ==
      """
      {
        "status": "success"
      }
      """