import pygame
import gpiozero
import time

pygame.mixer.init()

channel = pygame.mixer.Channel(0)

button_a = gpiozero.Button(2)
track_a = pygame.mixer.Sound('samples/song.wav')

channel.play(track_a, loops=-1)

while True:
    if button_a.is_pressed:
        channel.set_volume(1)
    else:
        channel.set_volume(0)
