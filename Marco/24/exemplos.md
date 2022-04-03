import express from "express";

const router = express.Router();

router.get("", ...);
router.post("", ...);
router.get("/:productId", ...);
router.put("/:productId", ...);
router.delete("/:productId", ...);

router.get("/history", ...);
router.get("/pdf", ...);
router.get("/:productId/reviews", ...);

## app.use("/api/product", router);

---

// src/routers/products.js

import express from "express";

const routerProducts = express.Router();

routerProducts.post("", ...);
routerProducts.get("", ...);
// ...

---

## app.use("/api/product/", routerProducts);

// src/routers/orders.js

import express from "express";

const routerOrders = express.Router();

routerOrders.post("", ...);
routerOrders.get("", ...);
// ...

app.use("/api/order/", routerOrders);

---

Exemplo 4
import express from "express"

const app = express()
const router = express.Router()

// Criação do controller que vai retornar uma mensagem.
const hello_world = (req, res) => {
res.json({message: "Hello World"})
}

// Rota GET que utiliza o controller hello_world
router.get('', hello_world)

// Também é possível deixar a função controladora direto na rota, sem precisar criá-la antes.
router.get('', (req, res) => {
res.json({message: "Hello World"})
})

app.listen(3000, () => console.log("Running at http://localhost:3000")

---

Exemplo 5

.
├── src
│ ├── app.js
│ │ // O ponto de entrada do projeto e
│ │ // deve ser o mínimo possível
│ ├── server.js
│ │ // Contém a conexão com o servidor
│ ├── services
│ │ // Contém todas as suas regras de negócios
│ ├── controllers
│ │ // Contém todas as funções das suas APIs
│ ├── middlewares
│ │ // Contém todos os seus middlewares
│ ├── routes
│ │ // Contém todas as suas rotas
│ ├── models
│ │ // Contém todos os seus esquemas
│ │ // e as funções deles
│ ├── tests
│ │ // Contém todos os testes
│ ├── utils*
│ │ // Contém funções que podem ser
│ │ // reutilizadas
│ ├── config*
│ │ // Contém arquivos de configuração
│ │ // para softwares de terceiros
│ └── types\*
│ // Contém os types para o TypeScript
│
├── package.json
│ // Contém detalhes do projeto,
│ // scripts e dependências
└── .gitignore
// Arquivos que você não quer botar no git
