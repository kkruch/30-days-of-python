import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.mail.ru"
port = 587
username = "sag.33@mail.ru"
password = "pass"
from_email = username
to_list = ["sag33.rus@gmail.com"]

class MessageUser():
    user_details = []
    messages = []
    email_messages= []
    base_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""

    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f"%(amount)
        detail = {
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail["email"] = email
        self.user_details.append(detail)
    
    def get_user_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_user_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_message = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail.get('email')
                if user_email:
                    user_data = {
                        'email': user_email,
                        'message': new_message
                    }
                self.messages.append(new_message)
            return self.messages
        return []
    
    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail['email']
                user_message = detail['message']
                try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username, password)
                    the_msg = MIMEMultipart('alternative')
                    the_msg['Subject'] = 'Billing update!'
                    the_msg['From'] =from_email
                    the_msg['To'] = user_email
                    part_1 = MIMEText(user_message, 'plain')
                    the_msg.attach(part_1)
                    email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                    email_conn.quit()
                except smtplib.SMTPException:
                    print('error sending message')
            return True
        return False


obj = MessageUser()
obj.add_user("Justin", 123.32, email='sag33rus@gmail.com')
obj.add_user("jOhn", 94.23, email='sag33rus@gmail.com')
obj.add_user("Sean", 93.23, email='sag33rus@gmail.com')
obj.add_user("Emilee", 193.23, email='sag33rus@gmail.com')
obj.add_user("Marie", 13.23, email='sag33rus@gmail.com')

obj.send_email()

"""examples
obj = MessageUser()
obj.add_user("Justin", 123.32, email='hello@teamcfe.com')
obj.add_user("jOhn", 94.23)
obj.add_user("Sean", 93.23)
obj.add_user("Emilee", 193.23)
obj.add_user("Marie", 13.23)
obj.get_details()

obj.make_messages()
"""



''''old stuff

default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""


def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            """
            Here's a simple solution to capitalize 
            everyone's name prior to sending
            """
            name = name[0].upper() + name[1:].lower() 

            """
            Did you get the bonus??
            """
            
            new_amount = "%.2f" %(amounts[i])
            new_msg = unf_message.format(
                    name=name,
                    date=text,
                    total=new_amount
                )
            i += 1
            print(new_msg)



make_messages(default_names, default_amounts)
'''