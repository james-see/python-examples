"""
What: bs4 get email from beautiful soup object
Author: James Campbell
Date: 2015-10-09
Updated Date: 3 July 2019
"""
from bs4 import BeautifulSoup
import re
import sys


def get_emails(soupcontent):
    """
        soupcontent: expected to be a bs4 object
        Description: This functions gets emails from bs4 object and returns a list
        """
    emaillist = []
    soupere = soupcontent.find_all(
        text=re.compile(
            r"\S[a-zA-Z0-9._%+-].*?[a-zA-Z0-9_%+-]+@[a-zA-Z0-9.-]+?\.[a-zA-Z]{2,4}?\b"
        )
    )
    for soupe in soupere:
        soupe = soupe.strip()
        if soupe == "":
            continue
        emaillist.append(soupe)
    return emaillist


htmlcontent = """<html><head></head><body>
<p>This is an email: james@jamescampbell.us and this is not: james.</p>"""
soupobject = BeautifulSoup(htmlcontent, "html.parser")
finallist = get_emails(soupobject)

# prove that it worked
for email in finallist:
    print(email)

sys.exit()
