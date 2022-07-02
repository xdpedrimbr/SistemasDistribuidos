from concurrent import futures
import time

import grpc
import grpc_pb2
import grpc_pb2_grpc

import paho.mqtt.publish as publish

dictValues = {}

class GreeterServicer(grpc_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.id = 0

    def createUser(self, request, context):
        self.id += 1
        dictValues[self.id] = request.valores

        return grpc_pb2.Users(id=self.id, valores = request.valores)

    def getUser(self, request, context):
        if request.id in dictValues:
            usuario = grpc_pb2.User(id = request.id, valores = dictValues[request.id])
            print(usuario)
        else:
            print("Nao existe o usuario desejado!")

        return usuario
    
    def deleteUser(self, request, context):
        if request.id in dictValues:
            dictValues.pop(request.id)
        else:
            print("Nao existe o usuario desejado!")
        response = grpc_pb2.mensagemVazia()

        return response 
    
    def updateUser(self, request, context):
        if request.id in dictValues:
            dictValues[request.id] = request.valores
        else:
            print("Nao existe o usuario desejado!")

        update = grpc_pb2.requestUpdate(id=request.id, valores=str(dictValues[request.id]))
        return update

    def userList(self, request, conext):
        usuarios = grpc_pb2.UserList()

        for i in dictValues:
            usuarios.users.append(grpc_pb2.User(id = i, valores=dictValues[i]))

        return usuarios

    def mosquittoUser(self, request, context):
        publish.single("user/client" + str(portaServer) + "/users", str(dictValues))

        response = grpc_pb2.mensagemVazia()
        return response

def escolhePorta():
    global portaServer

    print("Porta 1: 9091")
    print("Porta 2: 9092")
    print("Porta 3: 9093")
    print("Digite 4 para finalizar a escolha de portas")

    while True:
        port = 0
        portaServer = int(input("Escolha a porta que sera usada: "))

        if portaServer == 1:
            port = 9091
            break
        elif portaServer == 2:
            port = 9092
            break
        elif portaServer == 3:
            port = 9093
            break
        elif portaServer == 4:
            exit(0)

    serve(portaServer = port)

def serve(portaServer):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    grpc_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:" + str(portaServer))

    publish.single("user/client_" + str(portaServer) + "/users", str(dictValues))

    print("Rodando na porta: " + str(portaServer))
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    escolhePorta()
