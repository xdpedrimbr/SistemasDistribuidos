from concurrent import futures
import time

import grpc
import grpc_pb2
import grpc_pb2_grpc

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
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    grpc_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost: 9090")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
