import urllib, re, os
from bs4 import BeautifulSoup

visited = []
next_layer = []

def parse_url_bfs(html, layer = 1):
	"""
	parse url with bfs

	params html : root url
	params layer: visit layer

	"""
	cur_layer_n = 1
	cur_layer = []
	cur_layer.append(html)
	next_layer = []
	while (cur_layer_n <= layer):
		for link in cur_layer:
			page = urllib.urlopen(link)
			soup = BeautifulSoup(page.read(),"lxml")
			for a_line in soup.findAll('a', href=True):
				url = a_line.get("href")
				if url not in visited:
					visited.append(url)
					next_layer.append(url)
		cur_layer_n+=1

	print visited





def parse_prod_name(page):
	"""
	parse product name from page
	"""
	"""
	pd_name = []
	line = page.readline()
	while(line != None):
		if ("<li class=\"yui3-u-1 name\">" in line):
			print line
		line = page.readline()
	"""
	soup = BeautifulSoup(page.read(),"lxml")
	for li_line in soup.findAll("li", class_="yui3-u-1 name"):
		print li_line


if __name__ == '__main__':
	#page = urllib.urlopen("https://tw.buy.yahoo.com/?catitemid=26650&hpp=catid6365catitem26650")
	#page = urllib.urlopen("https://tw.buy.yahoo.com/")
	#parse_prod_name(page)
	#print (page.read())
	#soup = BeautifulSoup(page.read(), "lxml")
	#print (soup.a)
	#print (soup.a['class'])
	#print (soup.findAll('a', href=True)[0].get('href'))
	#for link in soup.findAll('a', href=True):

		#if "yui3-menu-label" in link['class']:
		#	print link.get(href)
	

	#parse_url_bfs("https://tw.buy.yahoo.com/", 1)
	page = urllib.urlopen("https://tw.buy.yahoo.com/?catitemid=52982&hpp=sub410catid3955catitem52982")
	parse_prod_name(page)