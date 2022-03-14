const pactum = require("pactum");
const expect = pactum.expect;
const { Before, Given, When, Then } = require("@cucumber/cucumber");
const { like } = require('pactum-matchers');

let spec = pactum.spec();
let response;

Before(() => {
  spec = pactum.spec();
});

Given("I make a GET request to url {string}", function (url) {
  spec.get(url);
});

When("I receive a response", async function () {
  response = await spec.toss();
});

Then("response should have a status {int}", async function (status) {
    expect(response).to.have.status(status);
});

Then("response data of size {int}", function (length) {
    expect(response).to.have.jsonLength('data', length);
});

Then("response data of type array", function () {
    expect(response).to.have.jsonSchema('data', {
        'type': 'array'
    });
});

Then(
  "response data matches schema",
  function () {
    expect(response).to.have.jsonMatch({'userId': 200,'firstName': like('Francis'),'lastName': like('Chelladurai'),'address': like('2 gfffgfg, hghgh, ghgh'),'phone': like('3245676778'),'email': like('francisgfg@test.com')});
  }
);

Then(
    "response data at index 0 matches schema",
    function () {
      expect(response).to.have.jsonMatch('data[0]', {'userId': like(200),'firstName': like('Francis'),'lastName': like('Chelladurai'),'address': like('2 gfffgfg, hghgh, ghgh'),'phone': like('3245676778'),'email': like('francisgfg@test.com')});
    }
  );