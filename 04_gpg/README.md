# Prática de GPG

## 1º - Criar Chave, Adicionar Foto e Publicar chave no Servidor
Criando Chave.<br>
![Criando Chave](prints/01.png)
<br>
Adicionando Foto.<br>
![ADD foto](prints/02.png)
<br>
Listando Chaves e Publicando no Servidor.<br>
![Criando Chave](prints/03.png)

## 2º - Importar a chave de outra pessoa do servidor remoto
Importando Chave.<br>
![Importando Chave](prints/04.png)

## 3º -  Enviar uma mensagem assinada em texto plano
Mensagem Assinada.<br>
![MSG Assinada](prints/05.png)
<br>
## 4º -  Enviar um arquivo .doc com assinatura em arquivo anexo
[Anexo](msg_sign.doc) <br>

## 5º -  Enviar um mensagem de texto criptografada em texto plano
Mensagem Criptografada.<br>
![MSG Encrypt](prints/06.png)


## 6º -  Enviar um arquivo criptografado
[Anexo](msg_encrypt.asc) <br>

## 7º -  Assinar a chave do seu colega e reenviar ao servidor
Listando Chaves.<br>
![Listando Chave](prints/07.png)
<br>
Assinando localmente.<br>
![lsign](prints/08.png)
<br>
Assinando porem sem alterar o quanto eu confio na chave.<br>
![sign](prints/09.png)
<br>
**OBS:** Mesmo assinando o nivel de confiança continua *desconhecida*
<br><br>
Alterando o nivel de confiança da chave.<br>
![trust](prints/10.png)
<br>
**OBS:** Alterei o nivel para *5*, neste caso o nivel de confiança se torna **plena**
<br><br>
Exportando para o servidor.<br>
![Exportando Chave](prints/11.png)


## 9º -  Revogar a sua chave no servidor remoto utilizando o certificado
Gerando o certificado de revogação.<br>
![Gerando o certificado](prints/12.png)
<br>
Revogando a chave.<br>
![Revogando a chave](prints/13.png)
<br>
Exportando para o servidor.<br>
![Exportando](prints/14.png)
