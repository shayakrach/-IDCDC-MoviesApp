import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import re
from setting import my_email, my_name, my_pass

# The domain name of gmail server
host = 'smtp.gmail.com'
port = 587

def movies_body_msg(movies_str):
    return f"""
Hi,

Your favourite movies:

{movies_str}

{my_name} ❤️
"""

def create_msg_container(addressee_email, mail_subject, body):
    # Create the container (outer) mail message.
    msg_container = MIMEMultipart()
    # Create the base text message.
    msg_container['From'] = my_email
    msg_container['To'] = addressee_email
    msg_container['Subject'] = mail_subject
    msg_container.attach(MIMEText(body, 'plain'))
    return msg_container

def sendmail(addressee_email, msg_container):
    try:
        text = msg_container.as_string()

        conn = smtplib.SMTP(host, port)
        conn.ehlo()
        conn.starttls()
        conn.login(my_email, my_pass)
        conn.sendmail(my_email, addressee_email, text)
        conn.quit()

        return 'Your favourites sent to {}'.format(addressee_email)

    except Exception as e:
        if type(e).__name__ == 'SMTPRecipientsRefused':
            return 'Invalid addressee email'
        else:
            return 'Something went wrong'

def send_mail_with_movies(addressee_email, movies_str):
    mail_subject = 'Your Favourite Movies'
    body = movies_body_msg(movies_str)

    msg_container = create_msg_container(addressee_email, mail_subject, body) 
    status_msg = sendmail(addressee_email, msg_container)
    return status_msg
    

def send_favourite_with_mail(addressee_email, movies_list):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", addressee_email):
        return 'Invalid email'

    if len(movies_list) == 0:
        return 'No favourite movies'
        
    movies_str = '\n'.join(movies_list)
    status_msg = send_mail_with_movies(addressee_email, movies_str)
    return status_msg
