FROM ubuntu
LABEL author="cityking"

RUN apt-get update \
    && apt-get install -y apt-transport-https vim iproute2 net-tools ca-certificates curl wget software-properties-common\
    && add-apt-repository ppa:jonathonf/python-3.6\
    && apt-get update\
    && apt-get install -y python3.6\
    && apt install -y python3.6-dev\
    && apt-get install -y python3-distutils\
    && wget https://bootstrap.pypa.io/get-pip.py\
    && python3.6 get-pip.py\
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2\
    && apt-get install -y language-pack-zh*\
    && ln -s /usr/bin/python3 /usr/bin/python\
ENV LANG C.UTF-8
