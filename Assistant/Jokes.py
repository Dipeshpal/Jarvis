import requests
from text_to_voice import tts

def joke(command):
    res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
    if res.status_code == requests.codes.ok:
        ans = str(res.json()['joke'])
        print(ans)
        tts(ans)
    else:
        tts('oops!I ran out of jokes')
