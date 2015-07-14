import urllib, re, os


def parse_prod_name(page):
	"""
	parse product name from page
	"""
	pd_name = []
	line = page.readline()
	while(line != None):
		if ("<li class=\"yui3-u-1 name\">" in line):
			print line
		line = page.readline()


if __name__ == '__main__':
	page = urllib.urlopen("https://tw.buy.yahoo.com/?catitemid=26650&hpp=catid6365catitem26650")
	parse_prod_name(page)
	#print (page.read())