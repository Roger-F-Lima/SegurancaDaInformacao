# implementar o algoritmo de vigenere (Relatório)
A cifra de Vigenère é um método de criptografia que usa uma série de diferentes cifras de César baseadas em letras de uma senha. Trata-se de uma versão simplificada de uma mais geral cifra de substituição polialfabética, inventada por Leone Battista Alberti cerca de 1465.. [Ver mais](https://pt.wikipedia.org/wiki/Cifra_de_Vigenère)
## Equipe
[Jardel Gonçalves](https://github.com/JardelGoncalves/)<br>
[Mara Vitória](https://github.com/maravitoria04/)
<br>

## O que você sabe fazer do que está sendo apresentado?
Apesar de precisar apenas da parte de descriptografia, tivemos que fazer a implementação da criptografia para de fato entender melhor o funcionamento do algoritmo para de fato apresentarmos a função de descriptografia, tendo isso em mente sei implementar completamente a cifra de vigenere.

## Como vocês dividiram/fizeram a atividade?
Tiramos um dia a tarde para fazermos o algoritmo juntos, por ser mais simples conseguimos terminar no mesmo dia, juntos implementamos`cifrar(m,k)` e `descifrar(mc,k)`, executamos o codigo que demorou um poquinho para acharmos a chave (muito usual na vida de um universitario da UFC). Como a execução demorava, decidimos usar arquivos para fazer uns backups, como possiveis chaves e ultima chave testada, e para isso decidimos implementar a função `brutalforce()` que mexe com arquivos em python para realiar essas funcionalidades<br>

## O que você aprendeu e o que ainda tem dificuldade?
Fazia tempo que não trabalho com arquivos então foi bom para dar uma revisada sobre isso e para começar a estudar expressões regulares. Minha dificuldade é trabalhar com expressões regulares onde não consegui trabalhar com elas em python.<br>

## Quanto tempo você gastou no total na atividade?
Gastamos 3 horas para implementar, agora para achar a chave... Foi tempo, menos de 24 horas.

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
6º Passo - não remova e nem renomei nenhum dos arquivos (`possiveis_chaves_satisfatoria.txt`,`ultima_chave.txt`,`tempo_de_execucao.txt`,`texto_cifrado_amor.txt` e o próprio programa `vigenere.py`)
7º Passo - Execute da seguinte forma: `python3 vigenere.py`
