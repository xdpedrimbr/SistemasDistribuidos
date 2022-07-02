## SistemasDistribuidos
Esse trabalho consistia em fazer a comunicação entre clientes e servidores usando o GRPC. Além disso, foi utilizado o Mosquitto, que é um protocolo para envio de dados entre aplicações e servidores.

## Implementação e Execução
Os códigos foram construídos em Python (3.10) e, como sistema operacional, o Ubuntu (22.04).

## Testes
Para fazer os testes, abra 3 terminais, no primeiro digite "python3 greet_server.py" e digite 1, para escolher a porta 9091. Após isso abrir o client com o comando "python3 greet_client.py" e copie e cole o teste1.txt. No terceiro terminal, digite "python3 mosquitto.py".
Para testar outra porta, faça o mesmo processo, porém no terminal que está o server, digite 2 e para o client copie e cole o teste2.txt.
Não foram implementadas todas as funções que foram pedidas na descrição do trabalho, faltou a de criação de tarefas.


## Dependências
sudo apt install python3-pip <br />
pip3 install --upgrade pip <br />
pip3 install grpcio-tools <br />
python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/grpc.proto<br />
<br />
Para poder executar o server e o client:<br />
python3 greet_server.py<br />
python3 greet_client.py
python3 mosquitto.py
