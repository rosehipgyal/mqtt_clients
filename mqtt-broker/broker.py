import paho.mqtt.client as mqtt

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {msg.payload.decode()}")

# Create client and bind callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to test Mosquitto broker
client.connect("test.mosquitto.org", 1883, 60)

# Start the loop
client.loop_forever()
