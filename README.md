## SistemasDistribuidos
Esse trabalho consistia em fazer a comunicação entre clientes e servidores usando o GRPC. Além disso, foi utilizado o Mosquitto, que é um protocolo para envio de dados entre aplicações e servidores.

## Implementação e Execução
Os códigos foram construídos em Python (3.10) e, como sistema operacional, o Ubuntu (22.04).

## Testes
Para fazer os testes, abra a pasta teste e copie e cole no terminal, o conteúdo dos arquivos .txt.

## Dependências
sudo apt install python3-pip
pip3 install --upgrade pip
pip3 install grpcio-tools
python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/grpc.proto

Para poder executar o server e o client:
python3 greet_server.py
python3 greet_client.py
