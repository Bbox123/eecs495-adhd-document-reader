import pygame
from gtts import gTTS

pygame.init()


def text2mp3(text: str, loc="var"):
    tts = gTTS(text)
    tts.save(loc+"/temp.mp3")
    return loc+"/temp.mp3"


def mp32aud(src="var/temp.mp3"):
    pygame.mixer.music.load(src)
    pygame.mixer.music.play()
    
    
def audio_stop():
    pygame.mixer.music.stop()
