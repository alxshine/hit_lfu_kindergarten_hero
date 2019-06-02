import pygame
from datetime import datetime

bpm = 120
millis_per_beat = 60000//bpm

queued_sounds = set()
buttons = [True, False, False, False]

pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=1024)

bass = pygame.mixer.Sound('samples/BD.wav')
clap = pygame.mixer.Sound('samples/kick.wav')
hh = pygame.mixer.Sound('samples/CHH.wav')
snare = pygame.mixer.Sound('samples/SD.wav')
cymbal = pygame.mixer.Sound('samples/kick.wav')
sounds = [bass, snare, hh, cymbal]

t = 0
last_beat = datetime.now()
while True:
    current_time = datetime.now()
    dt = current_time - last_beat
    delta_millis = dt.microseconds // 1000

    for i, v in enumerate(buttons):
        if v:
            queued_sounds.add(sounds[i])

    if delta_millis > millis_per_beat:
        print("beat")
        for s in queued_sounds:
            s.play()
        queued_sounds.clear()
        last_beat = current_time
