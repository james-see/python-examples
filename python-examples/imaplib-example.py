"""
What: Connect and get unread mail from imap example
Author: James Campbell
Date: 5 August 2019
"""
import time
import imaplib
import email
import sys
import os
import html2text
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

FROM_EMAIL = "scfith@gmail.com"
FROM_PWD = sys.argv[1]
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
detach_dir = '~/Downloads'


def get_body(email_message):
    """Get body of email message."""
    for payload in email_message.get_payload():
        break
    return payload.get_payload()


def two_way_email(server, uname, pwd):
    """Fetch and read latest unseen messages."""
    username = uname
    password = pwd
    readonly = True
    mail = imaplib.IMAP4_SSL(server)
    mail.login(username, password)
    mail.select("inbox", readonly)
    try:
        result, data = mail.uid('search', None, '(UNSEEN)')
        inbox_item_list = data[0].split()
        most_recent = inbox_item_list[-1]
        result2, email_data = mail.uid('fetch', most_recent, '(RFC822)')
        raw_email = email_data[0][1].decode("UTF-8")
        email_message = email.message_from_string(raw_email)

        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            att_path = os.path.join(detach_dir, filename)

            if not os.path.isfile(att_path):
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                print('Downloaded file:', filename)
        if email_message.is_multipart():
            for payload in email_message.get_payload():
                print('To:\t\t', email_message['To'])
                print('From:\t',     email_message['From'])
                print('Subject:', email_message['Subject'])
                print('Date:\t',email_message['Date'])
                for part in email_message.walk():
                    if (part.get_content_type() == 'text/plain') and (part.get('Content-Disposition') is None):
                        print('Body:\t',part.get_payload())
                break
        else:
            print('To:\t\t', email_message['To'])
            print('From:\t', email_message['From'])
            print('Subject:', email_message['Subject'])
            print('Date:\t', email_message['Date'])
            print('Thread-Index:\t', email_message['Thread-Index'])
            text = f"{email_message.get_payload(decode=True)}"
            html = text.replace("b'", "")
            h = html2text.HTML2Text()
            h.ignore_links = True
            output = (h.handle(f'''{html}''').replace("\\r\\n", ""))
            output = output.replace("'", "")
            print(output)

    except IndexError:
        print("No new email")


while True:
    two_way_email("imap.gmail.com", sys.argv[1], sys.argv[2])
    time.sleep(10)