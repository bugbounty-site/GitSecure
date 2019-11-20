import argparse, multiprocessing, re
import requests
from itertools import product

regex = {}
def getRegex():
	global regex
	regex = requests.get('https://raw.githubusercontent.com/dxa4481/truffleHogRegexes/master/truffleHogRegexes/regexes.json').json()

# def matchRegex(line, regex):
# 	reg = re.compile(regex)
# 	print(line)
# 	for match in re.findeiter(reg, line):
# 		print('Match found')

def readFile(file):
	#f = open('{dir}/{file}'.format(dir = directory, file = file))
	print(file)


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
