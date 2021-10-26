FROM python:3.9
LABEL maintainer="Ren Pang <rbp5354@psu.edu>"

RUN cd / && \
    git clone https://github.com/ain-soph/alpsplot.git && \
    cd ./alpsplot && \
    pip install --no-cache-dir -e .
WORKDIR /alpsplot/
