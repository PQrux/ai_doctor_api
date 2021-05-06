FROM debian:buster-slim
LABEL maintainer="PQrux (neubaner.guilherme@gmail.com)"
WORKDIR /media/api
RUN apt-get update
RUN apt-get install -y build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev libmagick++-dev wget r-base python3 python3-pip python3-venv
RUN Rscript -e 'install.packages("remotes")'
RUN Rscript -e 'install.packages("reticulate")'
RUN Rscript -e 'reticulate::install_miniconda()'
RUN Rscript -e 'install.packages("tensorflow"); library(tensorflow); install_tensorflow(version = "2.0.0")'
RUN Rscript -e 'remotes::install_github("decryptr/decryptr")'
RUN [ -d ./venv ] || (python3 -m venv ./venv)
RUN /bin/bash -c "source ./venv/bin/activate && pip install flask"
CMD /bin/bash -c "source ./venv/bin/activate && python ./app.py"