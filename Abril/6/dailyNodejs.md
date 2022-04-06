## Tratamento de erros no Express

A utilização de error comuns acaba se tornando muito confuso em um cotexto de larga escola, por isso acabamos usando o handle de errors. Por padrão adicionamos eles ao utils do projeto.

    class ErrorHandler extends Error {
        constructor(statusCode, message) {
        super();
        this.statusCode = statusCode;
        this.message = message;
    }
    }

Depois criamos uma função génerica:

    const handleError = (err, res) => {
      const { statusCode, message } = err;
      res.status(statusCode).json({
        status: "error",
        statusCode,
        message
      });
    };

    export default = {
    handleError,
    ErrorHandler
    }

para utilizarmos os erros, usamos:
throw new ErrorHandler
Utilizamos tambem o try, catch e no vatch usamos o next(error)

https://scoutapm.com/blog/express-error-handling
https://expressjs.com/en/guide/using-middleware.html
https://expressjs.com/en/guide/error-handling.html

## Services

O services, tem a função de retirar a responsabilidade do controller. Trazendo toda a lógica para ele.

    interface User {
      name: string;
      age: number;
      email: string;
    }

    class SignUserService {
      async execute({ name, age, email }: User) {
        const userRepository = new userRepository();

        const user = userRepository.create({ name, age, email });

        await userRepository.save(user);

        return user;
      }
    }

    export { SignUserService }


    route.post("/", validators.userSignup, async (req, res, next) => {
      const userDTO = req.body;

      const { user, company } = await UserService.Signup(userDTO);

      return res.json({ user, company });
    })

    export default class UserService {
      async Signup(user) {
        const userRecord = await UserModel.create(user);

        const companyRecord = await CompanyModel.create(userRecord);

        const salaryRecord = await Salarymodel.create(userRecord, companyRecord);

        await EmailService.startSignupSequence(userRecord);

        return { user: userRecord, company: companyRecord };
      }
    }

https://www.bmc.com/blogs/solid-design-principles/#:%7E:text=SOLID%20is%20an%20acronym%20that,some%20important%20benefits%20for%20developers.
https://softwareontheroad.com/ideal-nodejs-project-structure/#service

## TypeORM 06 - Criando Model/Entity com CLI

é necessario adicioanr ao ormconfig.ts

      ...
      "cli": {
        "entitiesDir": "src/entities",
        "migrationsDir": "src/migrations"
      }

para gerar um arquivo Entity diretament utilizamos:

yarn typeorm entity:create -n EntityName

https://www.devmedia.com.br/orm-object-relational-mapper/19056
https://typeorm.io/using-cli

## TypeORM 07 - Migrations Introdução

A utilização de migrations, é para solucionar o problema da recriação do banco de dados de um computador para o outro.

No typeorm temos os seguintes comandos:

typeorm migration:create
typeorm migration:generate
typeorm migration:run
typeorm migration:revert

https://juniorb2s.medium.com/migrations-o-porque-e-como-usar-12d98c6d9269
https://tasafo.wordpress.com/2012/10/13/controle-de-versao-em-bd/
https://typeorm.io/migrations
