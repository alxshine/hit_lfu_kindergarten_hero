import pygame
import gpiozero
from datetime import datetime

bpm = 120
millis_per_beat = 60000//bpm

queued_sounds = set()
button_0 = gpiozero.Button(14)
button_1 = gpiozero.Button(15)
button_2 = gpiozero.Button(21)
buttons = [button_0, button_1, button_2]

pygame.mixer.init(frequency=20050, size=-16, channels=2, buffer=512)

bass = pygame.mixer.Sound('samples/G.wav')
snare = pygame.mixer.Sound('samples/D.wav')
hh = pygame.mixer.Sound('samples/C.wav')
sounds = [bass, snare, hh]

t = 0
last_beat = datetime.now()
while True:
    current_time = datetime.now()
    dt = current_time - last_beat
    delta_millis = dt.microseconds // 1000

    for i, b in enumerate(buttons):
        if b.is_pressed:
            queued_sounds.add(sounds[i])

    if delta_millis > millis_per_beat:
        pygame.mixer.stop()
        for s in queued_sounds:
            s.play()
        queued_sounds.clear()
        last_beat = current_time
