$ yarn init -y

$ yarn add express

$ yarn add -D typescript ts-node nodemon

$ yarn add -D @types/node @types/express

**Configurar o typescript**

yarn tsc --init
>> cria o tsconfig

target : Usando esta opção, você pode especificar qual versão ECMAScript usar em seu projeto. As versões disponíveis são ES3(default), ES5, ES2015, ES2016, ES2017, ES2018, ES2019, ES2020 ou ESNEXT.
module : Com esta opção, você pode especificar qual gerenciador de módulo usar no código JavaScript gerado. Você pode escolher entre os seguintes valores none, commonjs, amd, system, umd, es2015, es2020 ou ESNext.
outDir : Com esta opção, podemos especificar onde produzir o código JavaScript “vanilla”.
rootDir : Especifica onde os arquivos TypeScript estão localizados.

---

yarn tsc --project ./  

Caso configure o rootDir

pode rodar apenas o yarn tsc

https://losikov.medium.com/part-1-project-initial-setup-typescript-node-js-31ba3aa7fbf1