## TypeORM 04 - Introdução ao padrão repository

Sere para divisão das responsabilidades que ficavam centralizadas no controller.

Os repositories fazem a conexão com o banco de dados.

Example:

    import usersDb from "../config/database";

    export const getUser = (req, res) => {
      const { id } = req.params;

      const user = usersDb.find((item) => item.id === id);

      return res.json(user);
    };

Exemplo de árvore de diretório:
├── ormconfig.ts
├── package-lock.json
├── package.json
├── src
│ ├── app.ts
│ ├── controllers
│ │ ├── createUser.controller.ts
│ │ ├── getUser.controller.ts
| | └── index.ts
│ ├── entities
│ │ └── User.ts
│ ├── migrations
│ ├── repositories
│ │ ├── index.ts
│ │ └── user
│ │ ├── index.ts
│ │ └── interface.ts
│ └── server.ts
├── tsconfig.json
└── yarn.lock

Padrao repository, utiliza na memsa pasta o repositorio e as funçoes de cada entity. Assim quando for criar ou fazer um get, tem que extender da classe do repository.

## TypeORM 05 - Relacionando entidades

Trabalha com o relacionamento padrão, ja visto antes. 1-1, many -1 , 1 - many, many-many.

TypeORM, oferece alguns opções para aprimior, eager,cascade, onDelete.

Exemplo One-to-One

    import {
    Entity,
    PrimaryGeneratedColumn,
    Column
    } from "typeorm";

    @Entity()
    export class Details {
    @PrimaryGeneratedColumn()
    id: number;

        @Column()
        gender: string;

        @Column()
        country: string;

    }

    import {
    Entity,
    PrimaryGeneratedColumn,
    Column,
    OneToOne,
    JoinColumn
    } from "typeorm";
    import { Details } from "./Details";

    @Entity()
    export class Customer {
    @PrimaryGeneratedColumn()
    id: number;

        @Column()
        name: string;

        @OneToOne(type => Details) @JoinColumn()
        details: Details;

    }

https://woliveiras.com.br/posts/construindo-uma-api-com-node-js-parte-2-melhorando-nossa-cria%C3%A7%C3%A3o-e-listagem-de-dados/

https://dev.to/fyapy/repository-pattern-with-typescript-and-nodejs-25da
