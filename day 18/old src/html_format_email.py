from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.mail.ru"
port = 587
username = "sag.33@mail.ru"
password = "pass"
from_email = username
to_list = ["sag33.rus@gmail.com"]


try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg = MIMEMultipart('alternative')
    the_msg['Subject'] = 'Hi there!'
    the_msg['From'] =from_email
    plain_text = 'Testing the message'
    html_txt = """\
    <html>
    <head></head>
    <body>
        <p>Hey!<br>
        Testing this email <b>message</b>. Made by <a href='http://joincfe.com'>Team CFE</a>.
        </p>
    </body>
    </html>
    """
    part_1 = MIMEText(plain_text, 'plain')
    part_2 = MIMEText(html_txt, 'html')
    the_msg.attach(part_1)
    the_msg.attach(part_2)

    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print('error sending message')