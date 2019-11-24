import argparse, multiprocessing, re
import requests
from itertools import product

regex = {}
def getRegex():
	global regex
	regex = requests.get('https://raw.githubusercontent.com/dxa4481/truffleHogRegexes/master/truffleHogRegexes/regexes.json').json()

def matchRegex(line):
	# create an array for returning matched keys
	matchedArray = []
	# for each key value pair in the dictionary (an item is a set of key/value pairs)
	for key, values in regex.items():
		#print(regexes)
		pythonReg = re.compile(values)
		# patern match regex in python
		match = pythonReg.search(line)
		# if match is not empty (has valid regex token)
		if match is not None:
			print(line)
			# append the key to the matched array so we track the instance of where plaintext token was found
			matchedArray.append(key)
		# return the array
		return matchedArray

def readFile(file):
	f = open('{dir}/{file}'.format(dir = directory, file = file))
	lines = f.readlines()
	for line in lines:
		matchRegex(line.strip())


if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--files', dest='filesToCheck', nargs="+") # adds all files passed into an array. The files are retrieved from git diff
	parser.add_argument('--repoloc', dest='dir') # gets argument from repoloc and assigns it to a string.
	args = parser.parse_args()
	global directory
	directory = args.dir
	getRegex()
	pool = multiprocessing.Pool(10)
	pool.map_async(readFile, args.filesToCheck)
	pool.close()
	pool.join()
