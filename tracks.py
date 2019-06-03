import pygame
import time

pygame.mixer.init()

channel = pygame.mixer.Channel(0)

track_a = pygame.mixer.Sound('samples/song.wav')

channel.play(track_a, loops=-1)

while True:
    for i in range(10):
        volume = i * 0.1
        channel.set_volume(volume)
        time.sleep(1)
