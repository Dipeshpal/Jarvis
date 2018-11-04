from gtts import gTTS
import random
import playsound
import os

# This function will convert Text in audio
def tts(audioInText):
    r1 = random.randint(1, 100000)
    r2 = random.randint(1, 100000)
    randfile = str(r1)+"File"+str(r2)+".mp3"
    text_to_speech = gTTS(text=audioInText, lang='en')
    text_to_speech.save(randfile)
    playsound.playsound(randfile, False)
    os.remove(randfile)
