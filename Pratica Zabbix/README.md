# PRÁTICA ZABBIX

## Dupla:
Jardel Gonçalves Ferreira

Mara Vitória Soares de Lima

## O QUE É?

## POR QUE MONITORAR?

## VANTAGENS E DESVANTAGENS

## INSTALAÇÕES

### SERVIDOR ZABBIX
Utilizamos uma maquina com o Debina 9

Tornando superusuário
```
su
```
Editando o arquivo sources.list
```
nano /etc/apt/sources.list
```
Deixe as sguintes configurações no arquivo:
```
deb http://ftp.br.debian.org/debian/ stretch main contrib non-free

deb http://security.debian.org/debian-security stretch/updates main non-free

deb http://ftp.br.debian.org/debian/ stretch-updates main non-free
```
Atualizando lista de repositórios
```
apt-get update
```
Baixando o pacote
```
wget http://repo.zabbix.com/zabbix/3.0/debian/pool/main/z/zabbix-release/zabbix-release_3.0-2+stretch_all.deb
```
Instalação do pacote
```
dpkg -i zabbix-release_3.0-2+stretch_all.deb
apt-get update
apt-get install zabbix-server-mysql zabbix-frontend-php zabbix-agent zabbix-get

```
Configurando Mysql
```
mysql -u root -p
create database zabbix character set utf8 collate utf8_bin;
grant all privileges on zabbix.* to zabbix@localhost identified by 'senha';
quit;
```
Criando Tabelas do banco
```
cd /usr/share/doc/zabbix-server-mysql
zcat create.sql.gz | mysql -uzabbix -p zabbix
```
Configurando o arquivo de configuração do Zabbix

Procure as linhas que, `DBHost=`, `DBName=`, `DBUser=` e `DBPassword=`
Caso estejam comentadas, descomente-as e adicione as seguintes configurações:
```
...
DBHost=localhost
...
DBName=zabbix
...
DBUser=zabbix
...
DBPassword=sua_senha
...
```
Inicie o Serviço:
```
service zabbix-server start
```

Configurando o fuso horário:
Descomente a(s) linha(s)
```
php_value date.timezone Europe/Riga
```
Altere para seu fuso horário:
```
php_value date.timezone America/Fortaleza
```
Reinicie o serviço apache2
```
service apache2 restart
```
#### *Opção de Instalação via Script:
[Acessar](https://github.com/JardelGoncalves/script-install-zabbix-debian)

Feito a instalação, vamos acessar a interface web para concluir de fato a instalação
```
http://seu_ip/zabbix/
```
#### Primeira Tela:

![imagem1](imagens/09.png)

#### Segunda Tela:

![imagem1](imagens/11.png)

**Possiveis Erros**

![imagem1](imagens/10.png)

***Corrigindo erro***
```
apt-get install php-mbstring php-bcmath php-xmlwriter php-xmlreader
service apache2 restart
```
#### Terceira Tela
Preencha os dados corretamente
![imagem1](imagens/12.png)

#### Quarta Tela
Deixe as informações padrões, apenas adicione um `nome`
![imagem1](imagens/13.png)

#### Quinta Tela

![imagem1](imagens/14.png)

#### Sexta Tela
Instalação concluida
![imagem1](imagens/15.png)

#### Tela de Login
Para acessar, o zabbix define as seguintes crenciais por padrão:
`Username: Admin` e `Password: zabbix`
![imagem1](imagens/16.png)




### MAQUINA CLIENTE (zabbix-agent)
Utilizamos uma maquina Ubuntu Server 16.04

Tornando superusuário:
```
sudo su
```

Baixando pacote:
```
wget http://repo.zabbix.com/zabbix/3.2/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.2-1+xenial_all.deb
```
Instalando pacote:
```
dpkg -i zabbix-release_3.2-1+xenial_all.deb
apt-get update
apt-get install zabbix-agent
```

Configurando agent:
```
nano /etc/zabbix/zabbix_agentd.conf
```
Procure as linhas `Server=` e `ServerActive=`, caso elas estejam comentadas, descomente-as e faça a seguinte configuração:
```
Server=ip-do-servidor
...
ServerActive=ip-do-servidor
```

Verifique se o agent está rodando:
```
service zabbix-agent status
```
Caso ele esteja dê o seguinte comando:
```
service zabbix-agent restart
```
Caso contrário:
```
service zabbix-agent start
```
## Matérial de apoio

## Atividade
