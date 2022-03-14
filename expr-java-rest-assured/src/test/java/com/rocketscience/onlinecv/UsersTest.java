package com.rocketscience.onlinecv;

import static io.restassured.RestAssured.given;
import static org.apache.http.HttpStatus.SC_CREATED;
import static org.apache.http.HttpStatus.SC_OK;
import static org.hamcrest.Matchers.both;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.either;
import static org.hamcrest.Matchers.endsWith;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.isA;
import static org.hamcrest.Matchers.notNullValue;

import io.restassured.http.ContentType;
import io.restassured.specification.RequestSpecification;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

public class UsersTest {
  RequestSpecification request = given().baseUri("http://localhost:3001/api")
      .header("Content-Type", "application/json")
      .accept(ContentType.JSON).request();

  @Test
  void ableToGetTheListOfUsers() {
    request.when()
        .get("/users")
        .then()
        .assertThat()
        .statusCode(SC_OK)
        .body("data.size()", is(10),
        "data[0].firstName", notNullValue(),
        "data[0].lastName", notNullValue(),
        "data[0].address", notNullValue(),
        "data[0].email", both(endsWith(".com")).and(containsString("@")),
        "data[0].phone", either(containsString("-")).or(containsString("x")),
        "data[0].userId", isA(Integer.class));
  }

  @ParameterizedTest
  @ValueSource(ints = { 200, 333 })
  void ableToGetAUser(int userId) {
    request.when()
        .get("/users/" + userId)
        .then()
        .assertThat()
        .statusCode(SC_OK)
        .body("userId", is(equalTo(userId)),
        "firstName", notNullValue(),
        "lastName", notNullValue(),
        "address", notNullValue(),
        "phone", notNullValue(),
        "email", notNullValue());
  }

  @Test
  void ableToCreateUser() {
    User user = User.builder()
        .firstName("Francis")
        .lastName("Chelladurai")
        .address("7 hello street, Hello, CT71, US")
        .phone("797976432")
        .email("gfghfh@ttt.com")
        .build();

    request.body(user)
        .when()
        .post("/users")
        .then()
        .assertThat()
        .statusCode(SC_CREATED)
        .body("status", is(equalTo("success")),
        "userId", notNullValue());
  }

  @Test
  void ableToUpdateUser() {
    User user = User.builder()
        .firstName("Francis")
        .lastName("Chelladurai")
        .address("7 hello street, Hello, CT71, US")
        .phone("797976432")
        .email("gfghfh@ttt.com")
        .build();

    request.body(user)
        .when()
        .put("/users/" + "202")
        .then()
        .assertThat()
        .statusCode(SC_OK)
        .body("status", is(equalTo("success")));
  }

  @Test
  void ableToDeleteUser() {
    request.when()
        .delete("/users/"+ 202)
        .then()
        .assertThat()
        .statusCode(SC_OK)
        .body("status", is(equalTo("success")));
  }
}
