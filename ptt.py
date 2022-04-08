import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/Beauty/M.1648100508.A.1F0.html"
c = {"over18":"1"}
response = requests.get(url, cookies=c)
html = BeautifulSoup(response.text)
links = html.find_all("a")
whitelist = ["jpg", "jpeg", "png", "gif"]
for link in links:
	href = link["href"]
	sub = href.split(".")[-1]
	if sub.lower() in whitelist:
		print(href)
