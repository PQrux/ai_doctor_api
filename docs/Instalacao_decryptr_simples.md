# INSTALAÇÃO DO DECRYPTR PARA DECODIFICAÇÃO DE CAPTCHAS DO SITE PGDAS.
- Faz o pull do debian buster slim e cria o container
```
docker pull debian:buster-slim
docker run --name ai_doctor -it debian:buster-slim
```
- Instala os pacotes necessários para o uso do R, do devtools e do decryptr
```
cd /root/
apt-get update
apt-get install -y build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev libmagick++-dev wget r-base
```
- Faz o download do decryptrModels
```
wget -O decryptModels.tar.gz https://api.github.com/repos/decryptr/decryptrModels/tarball/HEAD
```
- Gere um captcha no site da receita e envie para algum FTP do qual você possa fazer download usando o wget, recomendo: https://postimages.org/
```
wget -O captcha.png URL_DA_IMAGEM
```
- Faz a instalação do devtools decryptModels, decryptr e miniconda.
```
Rscript -e 'install.packages("devtools")'
Rscript -e 'devtools::install_local(path="/root/decryptModels.tar.gz")'
Rscript -e 'devtools::install_github("decryptr/decryptr")'
Rscript -e 'reticulate::install_miniconda()'
Rscript -e 'install.packages("tensorflow"); library(tensorflow); install_tensorflow()'
```
- Executa o decrypt para decodificar o captcha.
- Caso seja solicitada a instalação do Miniconda, aceite-a.
- A primeira vez que o comando é executado, será feito o download do tensorflow.
```
Rscript -e 'decryptr::decrypt("/root/captcha.png", "rfb")'
```
- Limpa os arquivos de instalação
```
rm /root/decryptModels.tar.gz /root/captcha.png
```

## FUNCIONOU ATÉ A INSTALAÇÃO DO MINICONDA