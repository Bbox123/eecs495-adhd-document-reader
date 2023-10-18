import pygame
import os
from gtts import gTTS


pygame.init()


def text2mp3(text: str, loc="var"):
    tts = gTTS(text)
    tts.save(loc+"/temp.mp3")
    return loc+"/temp.mp3"


def mp32aud(src="var/temp.mp3", time=-1, force_stop=False):
    pygame.mixer.music.load(src)
    pygame.mixer.music.play()
    if time > 0:
        pygame.time.delay(time)
        if force_stop:
            pygame.mixer.music.stop()
    
    
def audio_stop():
    pygame.mixer.music.stop()


def clear_cache(loc="var/temp.mp3"):
    try:
        os.remove(loc)
    except OSError:
        pass
    

def text2aud(text: str, time=-1, force_stop=False):
    text2mp3(text)
    mp32aud("var/temp.mp3", time, force_stop)
    

if __name__ == '__main__':
    clear_cache()
    text2aud("test, hello!", time=3000)
