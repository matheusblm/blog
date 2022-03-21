import jwt from "jsonwebtoken";
import express from "express";

const app = express();
const port = 3000;
const config = {
  secret: "my_random_secret_key",
  expiresIn: 60,
};

// Array para simular banco de dados em memória.
const users = [];

/*
Aplicação do middleware JSON para 
todas as rotas seguintes
*/
app.use(express.json());

// Rota para inserir um usuário.
app.post("/users", (req, res) => {
  users.push(req.body);
  return res.status(201).json(req.body);
});

// Rota para listar usuários.
app.get("/users", (req, res) => {
  return res.json(users);
});

app.listen(port, () => console.log(`Running in port ${port}`));

/* -------------------------------------- */

app.post("/login", (req, res) => {
  // Descontruímos o body para obter os dados de login.
  const { username, password } = req.body;

  /*
    Utilizando o username, buscamos
    algum item no array que satisfaça 
    a condição de igualdade.
    */
  const user = users.find((user) => {
    return user.username === username;
  });

  /*
    Validamos se o usuário foi encontrado e se a 
    senha confere com a encontrada
    */
  if (!user) {
    return res.status(401).json({
      message: "User not found.",
    });
  } else if (user.password != password) {
    return res.status(401).json({
      message: "User and password missmatch.",
    });
  }

  /*
    Geramos o token com o username como 
    identificador, passando o token, a chave 
    para decodificar e o tempo para expirar.
    */
  const token = jwt.sign({ username: username }, config.secret, {
    expiresIn: config.expiresIn,
  });

  // Retornamos com código 200 o token.
  return res.json({ token });
});

const authenticateUser = (req, res, next) => {
  /*
    O código a seguir é retirado de dentro
    do escopo da rota para reaproveitarmos em
    outras possíveis rotas
    */

  const token = req.headers.authorization.split(" ")[1];

  jwt.verify(token, config.secret, (err, decoded) => {
    if (err) {
      return res.status(401).json({ message: "Invalid Token" });
    }

    // Repare na última variável, vinda do JWT decodificado
    const user = users.find((user) => {
      return user.username === decoded.username;
    });

    /*
      Adicionamos o usuário ao request,
      assim todos os requests que utilizem
      esse MW terão acesso ao usuário.
      */
    req.user = user;
  });

  // Para continuar o fluxo do padrão MW.
  return next();
};

// Delete da própria conta somente
// autenticado, usando o MW que criamos

app.delete("/users", authenticateUser, (req, res) => {
  /*
  Acessando o usuário que foi 
  adicionado pelo MW no objeto req
  */
  const { user } = req;

  // Deletando o usuario logado do array.
  users.splice(user, 1);

  return res.status(204).send();
});

// Rota /whoami refatorada utilizando middleware
app.get("/whoami", authenticateUser, (req, res) => {
  const { cpf } = req.user;

  return res.json({ cpf: cpf });
});
