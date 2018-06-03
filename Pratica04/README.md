# Prática Tor

## Instalando o Tor

Baixando
```
curl -O -L https://www.torproject.org/dist/torbrowser//7.5.4/tor-browser-linux64-7.5.4_pt-BR.tar.xz
```
Descompactando
```
tar xvf tor-browser-linux64-7.5.4_pt-BR.tar.xz
```
Acessando o dirétorio gerado
```
cd tor-browser_pt-BR
```
Modificando alguns parametros para o funcionamento do Tor
```
sed -i 's/"`id -u`" -eq 0/"`id -u`" -eq x/' Browser/start-tor-browser
```
```
sed -i 's/The Tor Browser Bundle should not be run as root.  Exiting.//' Browser/start-tor-browser
```
