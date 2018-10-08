import smtplib

host = "smtp.gmail.com"
port = 587
username = "sag33.rus@gmail.com"
password = "testpassed"
from_email = username
to_list = ["sad33.rus@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hello there this is an email message")
email_conn.quit()



from smtplib import SMTP

abc = SMTP(host, port)
abc.ehlo()
abc.starttls()
abc.login(username, password)
abc.sendmail(from_email, to_list, "Hello there this is an email message")
abc.quit()


from smtplib import SMTP, SMTPAuthenticationError, SMTPException

pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, "wrongpassword")
    pass_wrong.sendmail(from_email, to_list, "Hello there this is an email message")
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("an error occured")

pass_wrong.quit()
