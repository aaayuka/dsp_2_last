from bs4 import BeautifulSoup
import requests
import time

url = "https://service.twr.co.jp/rinkai/public/DC/delay-certificate/status-list"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

import re

text_list = []

for tr in soup.find("tbody").find_all("tr"):
    td = tr.find("td")
    if td:
        text = td.text.strip() 
        if text == "掲載はありません。":
            text = "0\n" 
        elif re.search(r"\d+分", text):
            time = int(re.search(r"\d+", text).group())
            text = str(time) + "\n"
        else:
            text += "\n"
        text_list.append(text)

print("".join(text_list))

import sqlite3

path = '/content/'
db_name = 'dsp2_last.sqlite'
con = sqlite3.connect(path + db_name)
con.close()

con = sqlite3.connect(path + db_name)
cur = con.cursor()

sql_create_table_cars = 'CREATE TABLE dsp2_last_repo(delay_status int,　weather int);'

cur.execute(sql_create_table_cars)

con.close()

