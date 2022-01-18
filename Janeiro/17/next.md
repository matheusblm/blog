##Next

O web framework faz com que sua preocupacao fiquei em cima do produto. 
Faz a renderizacao no servidor - SSR
Geracao de estaticos - SSG
CSS-in-JS
zero configuration.
Otimizado para producao.

--
##Tipos de aplicacao 

Static Site - 
+Baixo uso do servidor, Pode ser enviado em uma CDN, melhor performance. 
-Tempo de build pose ser muito alto, dificuldade em escalar,dificuldade para constante mudancas.
*Para site simples, unica pessoa que publica, conteudo nao muda muito, quando a perfomance e extramemente importante.

Client Side Rendering -
+Permite paginas ricas em interacao sem recarregar, site rapido apos o load inicial, otimo para aplicacao web, possui diversas lib.
-Load inicial pode ser muito grande, perfomance imprevisivel, dificuldade no SEO. A maioria do conteudo nao e indexado.
*Quando nao tem necessidade de indexar info no google, Quando o usuario faz muitas interacoes na pagina e nao quer refresh, quando as infos vao ser diferentes para cada usuario.

Server Side Rendering(SSR)

+ Otimo em seo, meta tags previews mais adequados,melhor perfomance para o usuario(o conteudo vai ser visto mais rapido), codigo comporatilhado com Node, menor processamento no lado do usuario
-TTFB maior, o servidor vai preparar todo o conteudo para entregar, html maior. Reload completo nas mudancas de rota.
*Quando tem a necessidade de um SPA, mas precisa de um loagin mais rapido, quando o conteudo muda frequentemente, quando tem muitas paginas, e precisa de uma boa indexacacao no google.

Next tem suporte para os tres.

