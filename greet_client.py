from urllib import response
import grpc
import grpc_pb2
import grpc_pb2_grpc

class ClientServicer:
    def run(self):
        with grpc.insecure_channel('localhost:9090') as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            while True:
                print('1- Criar Client')
                print('2- Mostrar Client pelo ID')
                print('3- Deletar Client')
                print('4- Update Client')
                print('5- Listar todos os Clients')
                print('6- Finalizar sessao Client')
                rpc_call = input('Escolha o que voce gostaria de fazer: ')

                if rpc_call == "1":
                    self.createUser()
                elif rpc_call == "2":
                    self.getUser()
                elif rpc_call == "3":
                    self.deleteUser()
                elif rpc_call == "4":
                    self.updateUser()
                elif rpc_call == "5":
                    self.listAllUsers()
                
                if rpc_call == "6":
                    print("Sessao Client finalizada")
                    break
            

    def createUser(self):
        with grpc.insecure_channel('localhost:9090') as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            nomeUser = input("Digite o nome do client: ")
            emailUser = input("Digite o email do client: ")

            dictValues = {"nome": nomeUser, "email": emailUser}
            dictValuesString = str(dictValues)
            response = stub.createUser(grpc_pb2.User(id = 0, valores = dictValuesString))

            return dictValues

    def getUser(self, idBusca = -1):
        with grpc.insecure_channel('localhost:9090') as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            idBusca = int(input("Digite o ID do client: "))
            userId = grpc_pb2.requestUser(id = idBusca)
            response = stub.getUser(userId)
            print(response)

            if response.id == -1:
                print("Client not found")
            else:
                return response

    def deleteUser(self):
        deleteById = int(input("Digite o ID do client: "))
        response = self.getUser(deleteById)

        with grpc.insecure_channel('localhost:9090') as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            if response:
                response = stub.deleteUser(grpc_pb2.requestUser(id = deleteById))
                print("Client removido!")
            else:
                print("Client not found")

    def updateUser(self):
        updadeById = int(input("Digite o ID do client: "))
        response = self.getUser(updadeById)

        with grpc.insecure_channel('localhost:9090') as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            if response:
                nomeUser = input("Digite o nome do client: ")
                emailUser = input("Digite o email do client: ")

                dictValues = {"nome": nomeUser, "email": emailUser}

                dictValuesString = str(dictValues)
                response = stub.updateUser(grpc_pb2.requestUpdate(id = updadeById, valores = dictValuesString))

                print("Client atualizado!")
            else:
                print("Client not found")

    def listAllUsers(self):
        with grpc.insecure_channel('localhost:9090') as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            message = grpc_pb2.mensagemVazia()
            response = stub.userList(message)

            print(response)
        

if __name__ == "__main__":
    client = ClientServicer()
    client.run()
