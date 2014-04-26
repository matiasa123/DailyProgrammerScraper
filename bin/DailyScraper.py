import argparse
import urlparse
import urllib
from bs4 import BeautifulSoup

def parseInput():
	parser = argparse.ArgumentParser(
		description="Scrape challenges from reddit's /r/dailyprogrammer programming challenge",
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	#parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   #help='an integer for the accumulator')
	#parser.add_argument('--sum', dest='accumulate', action='store_const',
                   #const=sum, default=max,
                   #help='sum the integers (default: find the max)')

	args = parser.parse_args()
	print args.accumulate(args.integers)

def main():
	parseInput()

	url = "http://www.reddit.com/r/dailyprogrammer/"

	htmlText = urllib.urlopen(url).read()

	progSoup = BeautifulSoup(htmlText)

	table = progSoup.find(id="siteTable")

	#print table

if __name__=='__main__':
	main()
