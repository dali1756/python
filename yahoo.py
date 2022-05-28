import requests
import bs4
import pandas as pd

url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text , 'html.parser')

movies = soup.find_all("div", "release_movie_name")
movies_en = soup.find_all("div", "en")
levels = soup.find_all("div", "leveltext")
times = soup.find_all("div", "release_movie_time")

all_movie = []
for i, l in zip(movies, times):
    i = i.text.replace(" ","").split("\n")
    l = l.text.replace(" ","").split("\n")
    all_movie.append({"片名":i[2], "英文片名":i[5], "期待度":i[11], "上映日期":l[2]})

df = pd.DataFrame(all_movie)
print(df)
