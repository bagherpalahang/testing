import paho.mqtt.client as mqtt

broker_address = "broker.hivemq.com"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    client.subscribe("test_topic")

def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode()))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port, 60)
client.loop_forever()