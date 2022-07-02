import paho.mqtt.client as mqtt

class MqttClass():
    def __init__(self):
        pass

    def on_message(self, mqttc, obj, msg):
        print(msg.topic + " " + str(msg.payload)+"\n")

def server():
    client = mqtt.Client()
    clientClass = MqttClass()
    client.on_message = clientClass.on_message
    client.connect("localhost", 1883, 60)
    
    print("Mosquitto rodando...")

    client.subscribe('user/+/+', 0)
    client.loop_forever()

if __name__ == "__main__":
    server()