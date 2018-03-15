# Respostas das perguntas da aula s03e02

## O que foi feito da atividade e o que não foi feito.
## Com quem você fez.
## O que você sabe fazer do que está sendo apresentado.
## Como vocês dividiram/fizeram a atividade.
## O que você aprendeu e o que ainda tem dificuldade.
## Quanto tempo você gastou no total na atividade.



## 1- O que são chaves simetrica e assimetrica?
São  chaves usadas  para criptografar e descriptografar dados  provendo segurança na comunicação. Na prática, representa um segredo compartilhado entre duas ou mais partes que pode ser usado para manter uma  informação privada.<br>

## 2 - Quais são as diferenças? 
**Simétrica:** É usada uma única chave que é partilhada entre o emissor e o receptor. Desta forma, a chave que é usada para cifrar é a mesma que é usada para decifrar.Algoritmos que usam criptografia simétrica tendem a ser mais rápidos, no entanto não são tão seguros como os que usam criptografia assimétrica, uma vez que a chave usada para cifrar a informação é partilhada entre as várias máquinas.<br>

**Assimétrica:** Usam um par de chaves distintas (chave privada e chave pública). A chave pública é usada para cifrar (encriptar). A chave privada é usada para decifrar (desencriptar). A criptografia assimétrica é também conhecida por criptografia de chave pública.<br>

## 3 - Dê exemplos reais de algoritmo. 
RSA, RC4, DES, MD5, SHA <br>

## 4 - Dê exemplo de onde elas são usadas em conjunto. 
São usado em conjunto de forma que uma cifra os dados e a outra cifra a chave publica.


## 5 - O que é KDC? 
O KDC ( Centro Distribuidor de Chaves ) é um servidor centralizado também responsável pela autenticação dos usuários. O KDC autentica o usuário, também chamado principal, através de um ticket, que será utilizado para provar a identidade do usuário para os serviços disponíveis na rede. Ex: proxy


## 6 - Como funciona o GPG? 
 O GPG usa o método de chaves pública e privada (secreta) para assegurar a transferência de informações entre pares. Neste modelo cada usuário cria uma chave privada e outra pública. A privada é guardada consigo e não é passada adiante. A pública é enviada aos pares com os quais se deseja realizar trocas de informações de forma segura por criptografia.

## 7 - O que é um ICP?
(Infraestrutura de Chaves Públicas Brasileira)
é um conjunto de tecnologias  que garante às transações e aos documentos eletrônicos a segurança por meio do uso de um par de chaves. Uma delas é pública (de conhecimento geral), e a outra, privada (de conhecimento somente do proprietário), cujos dados estão consolidados em um “certificado digital”.

## 8 - Porque dá erro de cerficifado em alguns site inclusive no site da caixa?
Porque ou o site não possui certificado digital com alguma unidade certificadora ou o certificado está vencido.
