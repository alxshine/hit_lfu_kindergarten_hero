import paho.mqtt.client as mqtt
import pygame

pygame.mixer.init()
bg = pygame.mixer.Sound('song/BG.wav')
strings = pygame.mixer.Sound('song/STRINGS.wav')
guitar = pygame.mixer.Sound('song/GUITAR.wav')
sax = pygame.mixer.Sound('song/SAX.wav')

bg.play(loops=-1)

strings.set_volume(0)
strings.play(loops=-1)

guitar.set_volume(0)
guitar.play(loops=-1)

sax.set_volume(0)
sax.play(loops=-1)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("wifi")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = bytes.decode(msg.payload)
    if payload == 'violin_down':
        print("unmute violin track")
        strings.set_volume(1)
        print("unmuted violin track")
    elif payload == 'violin_up':
        print("mute violin track")
        strings.set_volume(0)
        print("muted violin track")
    elif payload == 'guitar_down':
        print("unmute guitar track")
        guitar.set_volume(1)
        print("unmuted guitar track")
    elif payload == 'guitar_up':
        print("mute guitar track")
        guitar.set_volume(0)
        print("muted guitar track")
    elif payload == 'drum_down':
        print("unmute drum track")
        sax.set_volume(1)
        print("unmuted drum track")
    elif payload == 'drum_up':
        print("mute drum track")
        sax.set_volume(0)
        print("muted drum track")
    else:
        print("Unknown message: " + payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.4.1", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
