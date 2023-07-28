import paho.mqtt.client as mqtt
import time

broker_address = "broker.hivemq.com"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    print('another line')

client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker_address, broker_port, 60)
client.loop_start()

try:
    while True:
        client.publish("test_topic", "Hello, MQTT!")
        time.sleep(1)

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
