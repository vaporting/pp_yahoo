import urllib, re, os
import urllib.request
from bs4 import BeautifulSoup

visited = []
interested = []
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
	num = 0
	while (cur_layer_n <= layer):
		for link in cur_layer:
			if len(link) > 23 and "https://tw.buy.yahoo.com" in link:
				try:
					#print (link + "\n")
					#num += 1
					#print (num)
					page = urllib.request.urlopen(link, timeout = 1)
					soup = BeautifulSoup(page.read(),"lxml")
					for a_line in soup.findAll('a', href=True):
						url = a_line.get("href")
						if url[0:2] == "/?" :
							url = "https://tw.buy.yahoo.com" + url
						if url[0:1] == "?":
							url = "https://tw.buy.yahoo.com/" + url
						if url not in visited:
							visited.append(url)
							next_layer.append(url)
				except Exception as e:
					#print ("except  :" + url + "\n")
					#print (e)
					pass
		cur_layer = list(next_layer)
		cur_layer_n+=1
	num = 0
	f = open("url_all.txt", "w+")
	for url in visited:
		f.write(url+ "\n")
		num += 1
		#print (url+"\n")
	f.close()
	print (num)
	





def parse_prod_name(page, f):
	"""
	parse product name from page
	"""
	soup = BeautifulSoup(page.read(),"lxml")
	for li_line in soup.findAll("li", class_="yui3-u-1 name"):
		print (li_line.get_text())
		f.write(li_line.get_text()+ "\n")


if __name__ == '__main__':
	parse_url_bfs("https://tw.buy.yahoo.com/", 3)
	#parse_url_bfs("https://tw.buy.yahoo.com/md/AddSupplier1.aspx", 3)
	"""
	f = open("yahoo_pd_name.txt", "w+")
	url_n = 0
	for url in visited:
		if "http" in url:
			url_n += 1
			print (url+'\n')
			page = urllib.request.urlopen(url, timeout = 1)
			parse_prod_name(page, f)
	f.close()
	print ("url_n : ", url_n)
	print ("visited size : ", len(visited))
	"""
	"""
	page = urllib.request.urlopen("https://www.litv.tv/vod/drama/content.do?brc_id=root&isUHEnabled=true&autoPlay=1&id=VOD00026656", timeout = 5)
	print (page.readline())
	print (page.read())
	soup = BeautifulSoup(page.read(),"lxml")
	"""