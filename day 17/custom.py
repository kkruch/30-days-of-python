import smtplib

host = "smtp.mail.ru"
port = 587
username = "sag.33@mail.ru"
password = "pass"
from_email = username
to_list = ["sag33.rus@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hello there this is an email message")
email_conn.quit()

from smtplib import SMTP

ABC = SMTP(host, port)
ABC.ehlo()
ABC.starttls()
ABC.login(username, password)
ABC.sendmail(from_email, to_list, "Hello there this is an email message")
ABC.quit()

from smtplib import SMTP, SMTPAuthenticationError, SMTPException

pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, password+'1')
    # pass_wrong.login(username, password)
    pass_wrong.sendmail(from_email, to_list, "Hello there this is an email message")
except SMTPAuthenticationError:
    print('Cant login')
except:
    print('an error occured')

pass_wrong.quit()