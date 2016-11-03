import requests
import json
import sys

urls = {"api_info example":"https://www.ob6.host/v2/api_info?uname=ade&apikey=u2eoo0n25wmcc85610s0ju3gb2np06w7","get pageid example":"https://www.ob6.host/v2/pageid?uname=ade&apikey=u2eoo0n25wmcc85610s0ju3gb2np06w7&pageid=100","get count of matched terms example":"https://www.ob6.host/v2/count?uname=ade&apikey=u2eoo0n25wmcc85610s0ju3gb2np06w7&term=hello","get pageids search by keyword example":"https://www.ob6.host/v2/search?uname=ade&apikey=u2eoo0n25wmcc85610s0ju3gb2np06w7&term=terrorists","check if domain exists example":"https://www.ob6.host/v2/domain?uname=ade&apikey=u2eoo0n25wmcc85610s0ju3gb2np06w7&d=elherbbgpkkk3gnk.onion","get page ids for a specific date example":"https://www.ob6.host/v2/ondate?uname=ade&apikey=u2eoo0n25wmcc85610s0ju3gb2np06w7&d=2016-10-20"}


def get_api_call(url,timeoutsetting=60):
	req = requests.get(url, timeout=timeoutsetting)
	try: return json.loads(req.text)
	except: return req.text

def main(allexamples=True,singleexample=None):
	global urls
	if not allexamples:
		url = urls[singleexample]
		returnedvalue = get_api_call(url)
		print (returnedvalue)
	else:
		for key in urls:
			print ("{} loading now...".format(key))
			print (".",end='')
			returnedvalue = get_api_call(urls[key])
			print ("returned json data:\n")
			print (returnedvalue)

if __name__ == "__main__":
	if len(sys.argv) > 1: # you can pass a domain manually to test collect
		u = []
		u.append(sys.argv[1])
		# if the command is help then the help screen should be displayed
		if u[0] in ['reqs','-?','?','-help','help','/help','/?','--help','-h']:
			print("\n\n")
			print(' _	   _	 ')
			print('| |_ ___| |___ ')
			print('|   | =|| | . |')
			print('|_|_|___|_|  _|')
			print('		  |_|  ')
			print('\n\n')
			print(color.YELLOW + 'Welcome to Obskura API TEST.' + color.END + '\n\nIt seems you are seeking help.\n\nTo run the app simply type' + color.RED + ' python3 casker.py override 1 ' + color.END + 'to force process the first batch id. \n\n\nThe following packages are required available via pip install:')
			print(color.RED + 'BeautifulSoup4, redis, chardet, langid, mysqlclient, PySocks' + color.END)
			exit('\nEnjoy the tool and read the docs in the readme.md file (open in any text editor)\nthat provides much more detailed instructions than this little bit of text.\n\n')
		else:
			if len(sys.argv) > 2: # example for test run python3 casker.py override 1 to force process batch:1
				if sys.argv[1] == 'override': # when you want it to force load specific example
					main(allexamples=False, singleexample=sys.argv[2])
			else:
				main()
	else:
		main() # if no domain passed in the command line then load all
