import requests
import json
import pandas as pd

headers = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}

url = "https://www.dcard.tw/_api/forums"
rs = requests.get(url)
response = rs.text
data = json.loads(response)

df_data = pd.DataFrame(data)
sort_data = df_data.sort_values(by = "subscriptionCount", ascending = False)
df_data.to_csv("dcard.csv")
print(sort_data[["name", "subscriptionCount"]][0:5])
