import sqlite3
from text_to_voice import tts
from voice_to_text import myListener
import smtplib

conn = sqlite3.connect('Assistant/Database/my_database.db')
c = conn.cursor()



def email(command):
    tts('Who is the recipient?')
    recipient = myListener()

    c.execute("SELECT Email from EmailContact WHERE Name=?", (recipient,))
    ans = c.fetchmany()

    if ans != None:
        tts('What should I say?')
        content = myListener()

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        #identify to server
        mail.ehlo()

        #encrypt session
        mail.starttls()

        #login
        tts("Enter Your key: ")
        mail.login('dipeshpal17@gmail.com', pw)

        # send email to user
        mail.sendmail('Dipesh Paul', ans, content)

        # confirmation email to admin
        datasend = content + ' : Mail sent to- ' + recipient
        mail.sendmail('Dipesh Paul', ans, datasend)

        #end mail connection
        mail.close()

        tts('Email sent.')

    else:
        tts('Contact Not Found or Try again')
