# Prática SQL Injection

## Dupla
Mara Vitoria e Jardel Gonçalves

Utilizamos a ferramenta em python para realizar esta prática web.


## Obtendo o banco
Neste comando, a ferramenta irá identificar o banco da aplicação.
![imagem1](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/01.png)

Como podemos ver, a ferramenta retorna os databases da aplciação web, que no caso são: acuart e o information_schema.

A linha em destaque mostra que a ferramenta criou um diretório referente ao site que está sendo utilizado nos testes.
![imagem2](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/02.png)

Na imagem a baixo, podemos ver o conteudo de um dos arquivos, nesse caso é o arquivo log, que guarda informações executadas.

![imagem3](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/03.png)

## Exibindo as tabelas
Nesta estapa executamos um comando para exibir as tabelas do banco `acuart`
![imagem4](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/04.png)

Saida

![imagem4](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/05.png)

## Exibindo as colunas de algumas tabelas
Nesta seção mostraremos um comando para exibir as colunas das tabelas, `artists`, `products` e `users`
![imagem5](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/16.png)

Saida

![imagem6](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/17.png)

## Exibindo informações da tabela de nosso interesse
A tabela que nos interessa é a dos `users`, então vamos ver as colunas:

Comando:

![imagem7](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/10.png)

Saida

![imagem8](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/11.png)

Agora vamos ver o conteudo das colunas: `address`,`email`,`name`,`pass` e `phone`

Comando:

![imagem9](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/12.png)

Saida

![imagem10](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/13.png)

## IMPORTANTE
Na saida das informações das colunas da tabela `users` a ferramenta cria um arquivo `.csv` como ilustrado na imagem a baixo

![imagem11](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/14.png)

Na figura abaixo podemos ver o arquivo,e as informações contidas nele

![imagem12](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/15.png)

![imagem12](https://github.com/JardelGoncalves/SegurancaDaInformacao/blob/master/Pratica01/Imagens/granfinaly.png)


**Todos os arquivos criado pela ferramenta estão disponiveis no direotio sqlmap deste git.**
