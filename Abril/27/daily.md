#### Node 25 trabalhando com emails

Nodemailer
O SMTP, Simple Mail Transfer Protocol, é o método mais usado para enviar e-mails entre vários servidores. Quase todos os sistemas de e-mail são baseados em SMTP.

Criamos o services que contem o transport que dentro tem o nodemailer.create transport recebendo as infomacoes do mail como
host, port, auth.

Depois criamos nosso controller que importa o transport, e dai criamos o mailOptions que e um objeto com os seguintes itens:
from, to, subject,text.
Ai usamos o metodo sendMail do transport, passando o mailoprtions como primeiro parametro e no segundo uma funcao anonima com handle de erro.

#### node 26 Criando templates de e-mail

Para a criacao de templates podemos utilizar o yarn add nodemailer-express-handlebars

#### Node 27 Trabalhando com Cloudinary

Servico em nuvem para gerencimaneto de imagens e videos usados em aplicacoes web, atraves dee api.
Podeemos adicionar o cloudinary como addon do heroku
heroku addons:create cloudinary:starter
usamos o heroku config para pegarmos a variavel de ambiente do cloudinary.
adicionamos no .env
CLOUDINARY_CLOUD_NAME=cloud_name
CLOUDINARY_API_KEY=apikey
CLOUDINARY_API_SECRET=apisecret
depois adicionamos ao nosso projeto
yarn add cloudinary
yarn add dotenv

### Recebdn oinput de arquivos com Multer

Multe = middlware para interpretar payload dee dados
opcpa so multer
const upload = multer({ dest: "uploads/" });
dest ou storage: onde armazenar os arquivos.
fileFilter: função para controlar quais arquivos são aceitos.
limits: limites dos dados enviados.
preservePath

o metodo upload depois de criado pode receber os metodos:
single("nome do arquivo") - envia aenas um arquivo
array("nome do arquivo", num de arv) - recebe varios
fields({name: nome do arquivo, maxCountL num de arq})
