from urllib import response
import grpc
import grpc_pb2
import grpc_pb2_grpc


class ClientServicer:        
    def escolhaPortas(self):
        while True:
            print("Porta 1: 9091")
            print("Porta 2: 9092")
            print("Porta 3: 9093")
            portaEscolha = int(input("Escolha a porta para iniciar: "))

            if portaEscolha > 3 and portaEscolha < 1:
                print("Escolha novamente, porta invalida!")
            else:
                return portaEscolha

    def run(self):
        while True:
            print('1- Criar Client')
            print('2- Mostrar Client pelo ID')
            print('3- Deletar Client')
            print('4- Update Client')
            print('5- Listar todos os Clients')
            print('6- Mosquitto')
            print('7- Finalizar sessao Client')
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
            elif rpc_call == "6":
                self.pubsub()
            else:
                print('Nao existe essa opcao!')
            
            if rpc_call == "7":
                print("Sessao Client finalizada")
                break
                

    def createUser(self):
        with grpc.insecure_channel('localhost:' + str(globalPort)) as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            nomeUser = input("Digite o nome do client: ")
            emailUser = input("Digite o email do client: ")

            dictValues = {"nome": nomeUser, "email": emailUser}
            dictValuesString = str(dictValues)
            response = stub.createUser(grpc_pb2.User(id = 0, valores = dictValuesString))

            return dictValues

    def getUser(self, idBusca = -1):
        with grpc.insecure_channel('localhost:' + str(globalPort)) as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            idBusca = int(input("Digite o ID do client: "))
            userId = grpc_pb2.requestUser(id = idBusca)
            response = stub.getUser(userId)
            print(response)

            if response.id == -1:
                print("Client not found")
            else:
                return idBusca

    def deleteUser(self):
        responseUser = self.getUser()

        with grpc.insecure_channel('localhost:' + str(globalPort)) as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            if responseUser:
                response = stub.deleteUser(grpc_pb2.requestUser(id = responseUser))
                print("Client removido!")
            else:
                print("Client not found")

    def updateUser(self):
        # updadeById = int(input("Digite o ID do client: "))
        responseUser = self.getUser()
        
        with grpc.insecure_channel('localhost:' + str(globalPort)) as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            if responseUser:
                nomeUser = input("Digite o nome do client: ")
                emailUser = input("Digite o email do client: ")

                dictValues = {"nome": nomeUser, "email": emailUser}

                dictValuesString = str(dictValues)
                response = stub.updateUser(grpc_pb2.requestUpdate(id = responseUser, valores = dictValuesString))

                print("Client atualizado!")
            else:
                print("Client not found")

    def listAllUsers(self):
        with grpc.insecure_channel('localhost:' + str(globalPort)) as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            message = grpc_pb2.mensagemVazia()
            response = stub.userList(message)

            print(response)

    def pubsub(self):
        with grpc.insecure_channel('localhost:' + str(globalPort)) as channel:
            stub = grpc_pb2_grpc.GreeterStub(channel)

            response = stub.userMosquitto(grpc_pb2.mensagemVazia())
            print(response)
        

if __name__ == "__main__":
    clientSer = ClientServicer()
    global globalPort
    port = clientSer.escolhaPortas()

    aux = 0

    print(port)
    if port == 1:
        aux = 9091
    elif port == 2:
        aux = 9092
    elif port == 3:
        aux = 9093

    globalPort = aux

    print("Conectando na porta " + str(aux))
    
    clientSer.run()
