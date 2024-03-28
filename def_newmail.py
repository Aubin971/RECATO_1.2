from email.message import EmailMessage
import ssl
import smtplib
from defin_recto2 import lire_csv_recto
from info_cato import get_password
import json
from tkinter import messagebox

info_config_id = "info.json"
def load_info_config_id():
    try:
        with open(info_config_id, "r") as file:
            data = json.load(file)
            return data.get("info", "info")
    except FileNotFoundError:
        messagebox.showwarning("Input Error",'''You are not already connected to an account, do it directly on CATO''')

Subject = 'Perte de votre mot de passe'
pswrd = (lire_csv_recto("recto_mail_.csv"))[0]
current_id = load_info_config_id()
concombre = (get_password(current_id))

def send_email(email_list):
    for person in email_list:
        email_sender = 'recto.entreprise@gmail.com'

        body = f"""
        Voici votre mot de passe : 
        {concombre}
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = person
        em['Subject'] = Subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,pswrd)
            smtp.sendmail(email_sender,person,em.as_string())

send_email([current_id])
