# PRÁTICA ZABBIX

## O QUE É?

## POR QUE MONITORAR?

## VANTAGENS E DESVANTAGENS

## INSTAÇÕES

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
#### Opção de Instalação via Script:
### MAQUINA CLIENTE (zabbix-agent)
