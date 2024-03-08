
import smtplib
from email.message import EmailMessage
from_email_addr ="grid1uk@aol.com"
from_email_pass ="lzsqmguwheqhapky"
to_email_addr ="graham.dimmock@hotmail.com"

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--subject")
parser.add_argument("-b", "--body")
args = parser.parse_args()


# Create a message object
print('Composing Email...')
msg = EmailMessage()
msg['Subject'] = args.subject
msg.set_content(args.body)
msg['From'] = from_email_addr
msg['To'] = to_email_addr

# Connecting to server and sending email
server = smtplib.SMTP('smtp.aol.com', 587)
# Comment out the next line if your email provider doesn't use TLS
server.starttls()
# Login to the SMTP server
server.login(from_email_addr, from_email_pass)

# Send the message
server.send_message(msg)
print('...Email sent')

#Disconnect from the Server
server.quit()
