#!/usr/bin/env python

import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msgtxt = """
<html>
  <head></head>
    <body>
    <p>*this is a test*<br>Hi {name}, please verify your Sugar Labs mail address by clicking the link below<br><b><a href="{url}">Confirm email</a></b></p>

    <small>If you are not able to click the link, please copy this address into your web browser:<br>
    <b>{url}</b>
    </small>
  </body>
</html>"""
server = "http://people.sugarlabs.org:5001/?verify="


f = open("mails.txt", "r")
mails = f.readlines()
f.close()

for mail in mails:
    name, email, vhash = mail.split("|")

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "[Sugar Labs] Please verify your mail address"
    msg['To'] = email
    msg['From'] = "members@sugarlabs.org"

    url = "%s%s" % (server, vhash)

    msghtml = MIMEText(msgtxt.format(url=url, name=name), 'html')
    msg.attach(msghtml)

    s = smtplib.SMTP('localhost')
    s.sendmail("members@sugarlabs.org", email, msg.as_string())
    s.quit()

    # Wait 5 seconds before sending the other
    time.sleep(5)
