import pygame
import os
from gtts import gTTS
import mutagen
from mutagen.mp3 import MP3


pygame.init()


def text2mp3(text: str, loc="var"):
    tts = gTTS(text)
    if not os.path.exists(loc):
        os.mkdir(loc)
    tts.save(loc+"/temp.mp3")
    return loc+"/temp.mp3"


def mp32aud(src="var/temp.mp3", time=-1, force_stop=False):
    pygame.mixer.music.load(src)
    pygame.mixer.music.play()
    if time > 0:
        pygame.time.delay(time)
        if force_stop:
            pygame.mixer.music.stop()

def audio_unload():
    pygame.mixer.music.unload()
    
def audio_stop():
    pygame.mixer.music.stop()

def audio_play():
    pygame.mixer.music.play()

def audio_pause():
    pygame.mixer.music.pause()

def audio_unpause():
    if get_audio_pos() > 0:
        pygame.mixer.music.unpause()
    else:
        audio_play()

def audio_rewind():
    pygame.mixer.music.rewind()

def get_audio_length():
    audio = MP3("var/temp.mp3")
    return audio.info.length

def get_audio_pos():
    return pygame.mixer.music.get_pos()


def clear_cache(loc="var/temp.mp3"):
    try:
        os.remove(loc)
    except OSError:
        pass

def get_audio_playing():
    return pygame.mixer.music.get_busy()  

def text2aud(text: str, time=-1, force_stop=False):
    text2mp3(text)
    mp32aud("var/temp.mp3", time, force_stop)
    

if __name__ == '__main__':
    clear_cache()
    text2aud("test, hello!", time=3000)
