# Implementação da Cifra Playfair
A cifra Playfair é uma substituição polialfabética em bloco bigrâmico (ou digrâmico). Nesta substituição,as letras são 
tomadas duas a duas (bloco bigrâmico), de acordo com regras aplicadas a uma grade de 5 por 5 que contém o alfabeto cifrante. Foi 
criada por Charles Wheatstone, a cifra Playfair foi apresentada em 1854 em um jantar oferecido pelo lorde Granville. [Ver mais](https://pt.wikipedia.org/wiki/Cifra_Playfair)
## Equipe
[Jardel Gonçalves](https://github.com/JardelGoncalves/)<br>
[Mara Vitória](https://github.com/)
<br>

## Desenvolvimento
A Mara Vitoria tem conhecimento na linguagem java, já eu tenho mais conhecimento em Python e sugeri fazermos esta implementação 
em python pela facilidade de compreensão da linguagem e pelo grau de dificuldade da implementação. Porem ela não programa em python a 
um bom tempo então tiramos um tempinho em dois dias para que eu pudesse ensinar algumas coisas de python para ela (sintaxe, estrutura de 
repetição, condicionais, entrada de dados e etc...).<br>
Com o basico aprendido começamos a implementar porem ainda não em codigo, desenvolvemos um fluxograma para facilitar a compreensão 
do problema e dividir o problema em partes. Tendo toda essa compreensão do problema, ela me ajudou a fazer algumas funções (
`montar_matriz()`, `imprimir_matriz_5x5()`, `monta_pares()` e `cifrar()`), as demais eu implementei só por questões de horarios/distancia.
<br>
Vimos algumas implementações da cifra Playfair porem muitas delas utilizava conceitos de Orientação a Objetos o que achamos que não 
seria necessario ([Ver implementação](https://siriarah.wordpress.com/2016/05/06/criptografia-cifra-playfair-em-python/)), encontramos 
outro que nos ajudou em algumas regras, como por exemplo bloco de duas letras seguidas iguais e algumas regras na parte de cifragem (
[Ver implementação](https://github.com/justworm/playfair-cipher/blob/master/playfair.py))<br>

## Informações
Foi utilizado a versão 3.x do Python, caso utilize a versão 2.x erros por causa de palavras acentuadas podem vir ocorrer para 
resolver esse problema é preciso adicionar no inicio do codigo: `#-*- coding:utf-8 -*-`.<br>
Utilizamos o sistema ubuntu 16.04 para executar o codigo.<br>

## Executando
1º Passo - Clone o repositorio.<br>
2º Passo - Abra o terminal `CTRL + ALT + T`.<br>
3º Passo - Navegue até onde se encontra o arquivo `.ZIP`(caso tenha baixado pela web).<br>
4º Passo - Utilize o comando `unzip nome-do-arquivo.ZIP`, caso dê comando não encontrado, instale utilizando `sudo apt-get install unzip` ( 
Esse passo pode ser pulado caso tenha clonado o repositorio via terminal).<br>
5º Passo - Acesse a diretorio que foi gerado.<br>
6º Passo - Execute da seguinte forma: `python3 Playfair.py`
