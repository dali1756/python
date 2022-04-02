import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
table = {
	"rating":[],
	"ja":[],
	"en":[],
	"type":[]
}

page = 58
while True:
	print("page:", page)
	url = "https://tabelog.com/tw/tokyo/rstLst/{}/?SrtT=rt".format(page)
	try:
		respone = urlopen(url)
	except HTTPError as e:
		print(e.code)
		if e.code == 400:
			print("最後一頁")
		df = pd.DataFrame(table)
		df.to_csv("tabelog.csv", encoding="utf-8", index=False)
		break
	page = page + 1
	html = BeautifulSoup(respone)
	rs = html.find_all("li", {"class":"list-rst"})
	for r in rs:
		en = r.find("a", {"class":"list-rst__name-main"})
		ja = r.find("small", {"class":"list-rst__name-ja"})
		rtype = r.find("li", {"class":"list-rst__catg"})
		prices = r.find_all("span", {"class":"c-rating__val"}) 
		rating = r.find("b", {"class":"c-rating__val"})
		
		print(en.text, ja.text, rtype.text)
		print("評價:", rating.text)
		print("Dinner:", prices[0].text)
		print("Lunch:", prices[1].text)
		print(en["href"])
		print("-" * 50)
		table["rating"].append(rating.text)
		table["ja"].append(ja.text)
		table["en"].append(en.text)
		table["type"].append(rtype.text)
