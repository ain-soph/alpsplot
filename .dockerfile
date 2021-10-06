FROM python:3.9
LABEL maintainer="Ren Pang <rbp5354@psu.edu>"

RUN pip install --no-cache-dir alpsplot && \
    cd / && \
    git clone https://github.com/ain-soph/alpsplot.git
WORKDIR /alpsplot/
