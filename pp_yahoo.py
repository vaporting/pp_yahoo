import urllib, re, os
import urllib.request
import concurrent.futures
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
		#print (li_line.get_text())
		f.write(li_line.get_text()+ "\n")

def divide_url_all():
	"""
	divide file in several file
	"""
	f = open("url_all.txt", "r+")
	url_amount = 0
	file_num = 1
	line = f.readline()
	sub_f = open("url_"+str(file_num)+".txt", "w+")
	while(line != ""):
		#print ("line : " + line )
		url_amount += 1
		sub_f.write(line)
		if url_amount > 33999:
			sub_f.close()
			url_amount = 0
			file_num += 1
			sub_f = open("url_"+str(file_num)+".txt", "w+")
		line = f.readline()
	sub_f.close()
	return file_num

def extract_file_and_parse(file_name, num):
	f = open(file_name, "r+")
	w_f = open("yahoo_pd_name_" + num + ".txt", "w+")
	line = f.readline().rstrip()
	while(line != ""):
		try:
			if "https://tw.buy.yahoo.com" in line:
				#print (line)
				page = urllib.request.urlopen(line, timeout = 1)
				parse_prod_name(page, w_f)
		except Exception as e:
			pass
		line = f.readline().rstrip()
	f.close()
	w_f.close()



def distribute_parse_pn(file_num):
	num = 1
	file_list = []
	num_list = []
	while(num <= file_num):
		file_list.append("url_"+str(num)+".txt")
		num_list.append(num)
		num += 1
	num = 1
	print (file_list)
	print (num_list)
	
	with concurrent.futures.ThreadPoolExecutor(max_workers=len(file_list)) as executor:
		while(num <= file_num):
			executor.submit(extract_file_and_parse, file_list[num-1], str(num_list[num-1]))
			num += 1




if __name__ == '__main__':
	#parse_url_bfs("https://tw.buy.yahoo.com/", 3)
	#file_num = divide_url_all()
	distribute_parse_pn(5)
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