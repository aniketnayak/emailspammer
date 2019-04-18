from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#FROM GMAIL ACCOUNT ONLY

host = "smtp.gmail.com"
port = 587
#type email
username = "enteremailhere@gmail.com"
#type email password
password ="enteremailpassword"
from_email = username
#enter recipients (can be more than 1)
to_list = ["randomemail@gmail.com","randomemail2@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.starttls()
email_conn.login(username, password)

the_msg = MIMEMultipart("alternative")
#subject of the email
the_msg['Subject'] = "spam spam lololol"
the_msg["From"] = from_email


plain_txt = "Testing the message"
#insert html code here (use https://html-online.com/editor/)
html_txt = """\
<html>
    <head></head>
    <body>
        <h1>lol spam</h1>
    </body>
</html>
"""

part_1 = MIMEText(plain_txt, 'plain')
part_2 = MIMEText(html_txt, "html")

the_msg.attach(part_1)
the_msg.attach(part_2)


i=0
print("Sending...")
#change the less than value to however many times you want the email to be sent
#example: i<80 sends 80 emails, i<10 sends 10 emails
while i<80:
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    print("Bot has sent " + str(i+1) + " so far") 
    i=i+1

print("All " + str(i) + " emails have been sent!")    
email_conn.quit()

