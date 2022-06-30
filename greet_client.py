import grpc
import grpc_pb2
import grpc_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = grpc_pb2_grpc.GreeterServicer(channel)
        print('1- Create User')
        print('\n2- Show User')
        print('\n3- Delete User')
        print('\n4- Update User')
        print('\n5- List all Users')
        rpc_call = input('Escolha o que voce gostaria de fazer: ')

        if rpc_call == "1":
            createUser()
        elif rpc_call == "2":
            getUser()
        elif rpc_call == "3":
            deleteUser()
        elif rpc_call == "4":
            updateUser()
        elif rpc_call == "5":
            print("Nao implementado")

def createUser(self):
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = grpc_pb2_grpc.GreeterServicer(channel)
        nomeUser = input("Digite o nome do client: ")
        emailUser = input("Digite o email do client: ")
        dictValues = {"nome": nomeUser, "email": emailUser}
        return dictValues

def getUser(self, idBusca = -1):
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = grpc_pb2_grpc.GreeterServicer(channel)
        idBusca = int(input("Digite o ID do client: "))
        userId = grpc_pb2.requestUser(id = idBusca)
        response = stub.getUser(userId)
        if response.id == -1:
            print("Client not found")
        else:
            return response

def deleteUser(self):
    deleteById = int(input("Digite o ID do client: "))
    response = self.getUser(deleteById)
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = grpc_pb2_grpc.GreeterServicer(channel)
        if response:
            response = stub.deleteUser(grpc_pb2.requestUser(id = deleteById))
            print("Client removido!")
        else:
            print("Client not found")

def updateUser(self):
    updadeById = int(input("Digite o ID do client: "))
    response = self.getUser(updadeById)
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = grpc_pb2_grpc.GreeterServicer(channel)
        if response:
            nomeUser = input("Digite o nome do client: ")
            emailUser = input("Digite o email do client: ")
            dictValues = {"nome": nomeUser, "email": emailUser}
            response = stub.updateUser(grpc_pb2.requestUpdate(id = updadeById, valores = dictValues))
            print("Client atualizado!")
        else:
            print("Client not found")

def listAllUsers(self):
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = grpc_pb2_grpc.GreeterServicer(channel)
        



if __name__ == "__main__":
    run()
