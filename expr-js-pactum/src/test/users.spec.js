const { spec, request } = require('pactum');
const { like } = require('pactum-matchers');

describe(('Able to manage users'), () => {
    before(()=> {
        request.setBaseUrl('http://127.0.0.1:3000')
    })
    
    it("GET /users", async() => {
      await spec()
        .get("/api/users")
        .expectStatus(200)
        .expectJsonLength('data', 10)
        .expectJsonSchema('data', {
            'type': 'array'
        })
        .expectJsonMatch('data[0]', {
            'userId': like(200),
            'firstName': like('Francis'),
            'lastName': like('Chelladurai'),
            'address': like('2 gfffgfg, hghgh, ghgh'),
            'phone': like('3245676778'),
            'email': like('francisgfg@test.com')
        })
    });

    it("GET /users/:userId", async() => {
        await spec()
          .get("/api/users/" + 200)
          .expectStatus(200)
          .expectJsonMatch({
              'userId': 200,
              'firstName': like('Francis'),
              'lastName': like('Chelladurai'),
              'address': like('2 gfffgfg, hghgh, ghgh'),
              'phone': like('3245676778'),
              'email': like('francisgfg@test.com')
          })
      });

      it("POST /users", async() => {
        await spec()
          .post("/api/users/")
          .withBody('{ "firstName":"Francis", "lastName":"Chelladurai", "address":"2 gfffgfg, hghgh, ghgh", "phone":"88764654", "email":"tyrytrytr@test.com" }')
          .expectStatus(201)
          .expectJsonMatch({
              'userId': like(200),
              'status': 'success'
          })
      });

      it("PUT /users", async() => {
        await spec()
          .put("/api/users/"+200)
          .withBody('{ "firstName":"Francis", "lastName":"Chelladurai", "address":"2 gfffgfg, hghgh, ghgh", "phone":"88764654", "email":"tyrytrytr@test.com" }')
          .expectStatus(200)
          .expectJsonMatch({
              'status': 'success'
          })
      });

      it("DELETE /users", async() => {
        await spec()
          .delete("/api/users/"+200)
          .expectStatus(200)
          .expectJsonMatch({
              'status': 'success'
          })
      });
})


