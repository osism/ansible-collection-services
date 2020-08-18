FROM golang:latest

RUN git clone https://github.com/zarplata/zabbix-agent-extension-mysql /go/src/zabbix-agent-extension-mysql \
    && apt-get update \
    && apt-get install -y go-dep
WORKDIR /go/src/zabbix-agent-extension-mysql
RUN make
