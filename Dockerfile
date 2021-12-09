FROM python
LABEL maintainer="Ren Pang <rbp5354@psu.edu>"

RUN cd / && \
    git clone https://github.com/ain-soph/alpsplot.git && \
    cd ./alpsplot && \
    pip install --no-cache-dir --upgrade -e .
WORKDIR /alpsplot/
