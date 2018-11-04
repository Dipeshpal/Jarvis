from text_to_voice import tts
from Assistant import Assistant
from voice_to_text import myListener as vtt

cout = 0
while True:
    if cout == 0:
        tts("Hello Mr. Dipesh! , how can I help you?")
        cout = cout+1
    else:
        command = vtt()
        Assistant.assistant(command)

