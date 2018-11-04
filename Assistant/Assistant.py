from text_to_voice import tts
from Assistant import openurl as op
from Assistant import Jokes as jo
from Assistant import Weather as wea
from Assistant import Email as em
from Assistant import AddEmail as AE

# Assistant Here
def assistant(command):
    # if / elif statements for executing commands

    ### Features ###
    if 'open reddit' in command:
        op.openReddit(command)

    elif 'joke' in command:
        jo.joke(command)

    elif 'weather' in command:
        wea.weatherFun(command)

    elif 'email' in command:
        em.email(command)

    elif 'add contact' in command:
        AE.addEmail(command)

    ### Chat ###
    elif 'what\'s up' in command:
        print('Just doing my thing')
        tts('Just doing my thing')
