import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text,"lxml")
# print(soup)

table = soup.find("table",class_="ih-td-tab auction-tbl")
# print(table.text)

headers = table.find_all("th")
# print(headers)

titles = []
for i in headers:
    # print(i.text)
    title = i.text
    titles.append(title)
# print(titles)
df=pd.DataFrame(columns=titles)

rows = table.find_all("tr")
# print(rows)
for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    # print(data)
    row = [tr.text for tr in data]
    row.insert(0,first_td)
    # print(row)
    l = len(df)
    df.loc[l] = row
print(df)

df.to_csv("IPL_Auction_stats_2022.csv")

