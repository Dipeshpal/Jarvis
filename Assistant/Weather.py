from weather import Weather
from text_to_voice import tts
import re


def weatherFun(command):
    reg_ex = re.search('weather (.*)', command)
    if reg_ex:
        city = reg_ex.group(1)
        weather = Weather()
        location = weather.lookup_by_location(city)
        condition = location.condition()
        tts('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))
