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

    // index.ts

    import { getRepository } from "typeorm";
    import { Details } from "./Details";
    import { Customer } from "./Customer";

    // crie uma função assíncrona
    const asyncFunctionRepository = async () => {
    const detailsRepository = getRepository(Details);

    const data = {
    gender: "female",
    country: "brazil"
    };

    const details = detailsRepository.create(data);

    await detailsRepository.save(details)
    }

    const asyncFunctionCustomer = async () => {
    const customerRepository = getRepository(Customer);

    const details = detailsRepository.create(data);

    const data = {
    name: "customer1",
    details: details
    };

    const customer = customerRepository.create(data);

    await customerRepository.save(customer)
    }

One-to-Many e Many-to-One

// project.ts

    import {
    Entity,
    PrimaryGeneratedColumn,
    Column,
    ManyToOne
    } from "typeorm";
    import { Student } from "./Student";

    @Entity()
    export class Project {
     @PrimaryGeneratedColumn()
    id: number;

    @Column()
    projects: string;

    @ManyToOne(type => Student, student => student.projects)
    student: Student;
    }

// student.ts

    import {
    Entity,
    PrimaryGeneratedColumn,
    Column,
    OneToMany
    } from "typeorm";
    import { Project } from "./Project";

    @Entity()
    export class Student {
     @PrimaryGeneratedColumn()
    id: number;

    @Column()
    name: string;

    @OneToMany(type => Project, project => project.student)
    projects: Project[];
    }

**Você pode omitir @JoinColumn em uma relação @ManyToOne / @OneToMany.
@OneToMany não pode existir sem @ManyToOne. Se você quiser usá-la, @ManyToOne é necessária. **

// index.ts

    import { getRepository } from "typeorm";
    import { Project } from "./Project";
    import { Student } from "./Student";

    const projRepository = getRepository(Project);

    const data = { projects: "database management" };

    const proj1 = await projRepository.save(data);

    const proj2Repository = getRepository(Project);

    const data2 = { projects: "web application" };

    const proj2 = await proj2Repository.save(data2);

    const studRepository = getRepository(Student);

    const stud = {
      name: "Student1",
      projects: [proj1, proj2]
    };

    await studRepository.save(stud);

Many-to-Many

    // classes.ts

    import {
    Entity,
    PrimaryGeneratedColumn,
    Column
    } from "typeorm";

    @Entity()
    export class Classes {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    name: string;
    }

// student.ts

    import {
      Entity,
      PrimaryGeneratedColumn,
      Column,
      ManyToMany,
      JoinTable
    } from "typeorm";

    import { Classes } from "./Classes";

    @Entity()
    export class Student {
      @PrimaryGeneratedColumn()
      id: number;

      @Column()
      name: string;

      @Column()
      subjects: string;

      @ManyToMany(type => Classes) @JoinTable()
      classes: Classes[];
    }

https://woliveiras.com.br/posts/construindo-uma-api-com-node-js-parte-2-melhorando-nossa-cria%C3%A7%C3%A3o-e-listagem-de-dados/

https://dev.to/fyapy/repository-pattern-with-typescript-and-nodejs-25da

https://typeorm.io/relations

https://levelup.gitconnected.com/complete-guide-to-using-typeorm-and-typescript-for-data-persistence-in-node-js-module-bfce169959d9
