import urllib, re, os
import urllib.request
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
	visited.append(html)
	next_layer = []
	while (cur_layer_n <= layer):
		for link in cur_layer:
			if "http" in link:
				#print (link + "\n")
				page = urllib.request.urlopen(link)
				soup = BeautifulSoup(page.read(),"lxml")
				for a_line in soup.findAll('a', href=True):
					url = a_line.get("href")
					if url[0:2] == "/?":
						cut_pos = link.find("/?sub")
						url = link[:cut_pos] + url
						#print (url)
					if url not in visited:
						visited.append(url)
						next_layer.append(url)
		cur_layer = list(next_layer)
		cur_layer_n+=1
	
	f = open("url_all.txt", "w+")
	for url in visited:
		f.write(url+ "\n")
		#print (url+"\n")
	f.close()
	





def parse_prod_name(page, f):
	"""
	parse product name from page
	"""
	soup = BeautifulSoup(page.read(),"lxml")
	for li_line in soup.findAll("li", class_="yui3-u-1 name"):
		print (li_line.get_text())
		f.write(li_line.get_text()+ "\n")


if __name__ == '__main__':
	parse_url_bfs("https://tw.buy.yahoo.com/", 2)
	#parse_url_bfs("https://tw.buy.yahoo.com/?sub=1", 1)
	
	f = open("yahoo_pd_name.txt", "w+")
	url_n = 0
	for url in visited:
		if "http" in url:
			url_n += 1
			print (url+'\n')
			page = urllib.request.urlopen(url)
			parse_prod_name(page, f)
	f.close()
	print ("url_n : ", url_n)
	print ("visited size : ", len(visited))