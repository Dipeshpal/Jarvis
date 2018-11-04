import speech_recognition as sr

# This function will convert audio in text
def myListener():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am ready to hear command from you, Say anything")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myListener()
    return command
