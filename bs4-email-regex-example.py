# bs4 get email from beautiful soup object
# author: James Campbell
# date: October 9th 2015
from bs4 import BeautifulSoup
import re

def get_emails(soupcontent):
	"""
	This functions gets emails from bs4 object and return back a list of them
	"""
	emaillist = []
	soupere = soupcontent.find_all(text=re.compile(r"\S[a-zA-Z0-9._%+-].*?[a-zA-Z0-9_%+-]+@[a-zA-Z0-9.-]+?\.[a-zA-Z]{2,4}?\b"))
	for soupe in soupere:
		soupe = soupe.strip()
		if soupe == '':
			continue
		emaillist.append(soupe)
	return emaillist

htmlcontent = "<html><head></head><body><p>This is an email: james@jamescampbell.us and this is not: james.</p>"
soupobject = BeautifulSoup(htmlcontent,"html.parser")
finallist = get_emails(soupobject)
for email in finallist:
	print (email)

exit()