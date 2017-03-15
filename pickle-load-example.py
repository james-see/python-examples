# pickle load example
import pickle
import random
import json

with open('discordia.pkl', 'rb') as f:
	discordia = pickle.load(f)

def getran(tex):
	texter = random.choice(tex)
	if len(texter) < 140 and len(texter) > 0:
		return texter
	else:
		globular = getran(tex)
	return globular

def to140(data):
	loser = []	
	for listitem in data:
		if len(listitem) < 140 and len(listitem) > 0:
			loser.append(listitem)
	return loser

#data140 = to140(discordia)
#jsondata = json.dumps(data140)
#with open('discordia.json','w') as f:
#	f.write(jsondata)

print(getran(discordia))
exit('there ya go')