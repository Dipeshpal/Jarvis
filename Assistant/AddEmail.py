from os import mkdir
import sqlite3
import random

r1 = random.randint(1, 100000)

from text_to_voice import tts
from voice_to_text import myListener



try:
    conn = sqlite3.connect('Assistant/Database/my_database.db')
except sqlite3.OperationalError:
    mkdir('Assistant/Database')
finally:
    conn = sqlite3.connect('Assistant/Database/my_database.db')

c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS EmailContact(Id	INTEGER PRIMARY KEY AUTOINCREMENT, Name	TEXT, Email	TEXT)")

def createEmail(name, email):
    create_table()
    c.execute("INSERT INTO EmailContact(Name, Email) VALUES (?, ?)",(name, email))
    conn.commit()

def addEmail(command):
    tts("Enter Name")
    name = input("Enter Name: ")
    tts("Enter Email")
    email = input("Enter Email: ")
    tts("Is it ok or you want to change something")
    command1 = myListener()
    if 'ok' in command1:
        createEmail(name, email)
        tts('contact saved')
    elif 'change it' in command1:
        tts('Okay, let\'s try again')
        addEmail(command1)
    c.close()
    conn.close()
