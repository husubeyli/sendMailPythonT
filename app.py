from smtplib import SMTP 
from password import *



#Simple Mail Transfer Protocol
try:
    subject = 'Husubayli'
    message = 'Salam Aleykum'
    content = "Subject: {0}\n\n{1}".format(subject, message)

    # Creditionals
    owner_gmail_data = emailConfig()
    myMailAdress = owner_gmail_data["email"]
    password = owner_gmail_data["password"]


    # to Send Email
    sendTo = 'husubeyli@gmail.com'


    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress, password)
    mail.sendmail(myMailAdress, sendTo, content.encode('utf-8'))
    print('Email gonderilme islemi ugurla tamamlandi')
except Exception as e:
    print("Xeta yarandi!\n{0}".format(e))
