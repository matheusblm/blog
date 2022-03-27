// app.js
import express from "express";

const app = express();
const usersArr = [ ];

app.use(express.json());


// Rotas
app.post("/users", (req, res) => {
  const user = req.body;

  usersArr.push(user);
  return res.status(201).json(user);
});

app.get("/users", (req, res) => {
  return res.json(usersArr);
});

export default app;

// Para a execução dos testes, o app.listen() não deve ser 
// executado junto com as rotas. 

----

TESTES

// users.test.js
import { describe, expect, it } from "@jest/globals";
import request from "supertest";
import app from "./app";

const user = {
  username: "testuser",
  password: "12345",
};

describe("Users Tests", () => {
  it("Should create a User 1", async () => {
    const response = await request(app).post("/users").send(user);

    expect(response.statusCode).toBe(201);
    expect(response.body).toStrictEqual(user);
  });

  it("Should create a User 2", async () => {
    const response = await request(app).post("/users").send(user);

    expect(response.statusCode).toBe(201);
    expect(response.body).toStrictEqual(user);
  });

  it("Should get users", async () => {
    const response = await request(app).get("/users");

    expect(response.statusCode).toBe(200);
    expect(response.body.length).toBe(2);
  });
});