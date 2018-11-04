import re, webbrowser
from text_to_voice import tts



def openReddit(command):
    reg_ex = re.search('open reddit (.*)', command)
    url = 'https://www.reddit.com/'
    if reg_ex:
        subreddit = reg_ex.group(1)
        url = url + 'r/' + subreddit
    print("Opening Reddit")
    tts("Opening Reddit")
    webbrowser.open(url)
