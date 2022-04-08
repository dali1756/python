import os
import json
from urllib.request import urlopen, urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

for i in range(6):
	month = str(i + 1)
	print("月份:", month)
	
	base = "google/" + month
	if not os.path.exists(base):
	    os.makedirs(base)

	url = "https://www.google.com/doodles/json/2021/" + month + "?hl=zh-TW"
	response = urlopen(url)
	pics = json.load(response)
	for p in pics:
		print(p["title"])
		imgurl = "https:" + p["high_res_url"]
		print(imgurl)
		fn = base + "/" + imgurl.split("/")[-1]
		urlretrieve(imgurl, fn)
		print("-" * 100)
