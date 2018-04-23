#!/usr/bin/python3
# Author: James Campbell
# What: Parse divs from transactions.html file
# Date: 06-07-2017
import csv
from bs4 import BeautifulSoup, SoupStrainer

with open('/Users/jc/Downloads/transactions.html') as f:
	#transaction_strainer = SoupStrainer('div', {'class': 'transaction'})
	#soup = BeautifulSoup(f, 'html.parser',parse_only=transaction_strainer)
	soup = BeautifulSoup(f,'html.parser')
	listOfTransactions = soup.findAll('div',{'class':'transaction'})
	print(listOfTransactions[5])
	with open('/Users/jc/Downloads/transactions.csv', 'w', newline='') as tcsv:
		tscvwritten = csv.writer(tcsv, delimiter=',')
		for item in listOfTransactions:
			descriptionOfTransaction = item.find('div',{'class':'description'}).text
			amountOfTransaction = item.find('span',{'class':'tx-amount'}).text
			dateOfTransaction = item.find('div',{'class':'timestamp'}).text
			tscvwritten.writerow([dateOfTransaction,amountOfTransaction,descriptionOfTransaction])
	#print(listOfTransactions[0].find('span',{'class':'tx-amount'}).text)
	#print(len(maindivs))
	#print(len(amounts))
	print("processed {} transactions".format(len(listOfTransactions)))

	#print(amounts[1])
exit('working so far')