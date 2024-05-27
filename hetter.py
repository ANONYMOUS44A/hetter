#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests, lxml
import os

os.system("clear")

print("""
         _, ,_    ___  ________   ________    ___  ___
        / | | \\  / _/ /__,  ,__\\ /__,  ,__\\  / _/ /   \\
       _| | | |_/ /______\\  /_______\\  /____/ /___| + |__
      / | |_| | \\ \\ WEARE || THEFUTUR||TRUST\\ \\US |   /_ \\
      \\_| ___,|_/ /_______||_________||_____/ /___|  _  |/
        | | | | \\ \\_,     ||         ||     \\ \\_, |  | \\ \\
        \\_| |_/  \\__\\     <>         <>      \\__\\ <> |__>

                     .:: PENTAGONE GROUP ::.
""")

dork = input("{ Search Query }=> ")
number = input("{ Results Qty }=> ")
output = input("{ Output File }=> ")

params = {
    "q": dork, # query example
    "hl": "en",          # language
    "gl": "uk",          # country of the search, UK -> United Kingdom
    "start": 0,          # number page by default up to 0
    "num": number           # parameter defines the maximum number of results to return.
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

page_limit = 10          # page limit, if you do not need to parse all pages
page_num = 0

links = []

while True:
    page_num += 1

    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, 'lxml')

    for result in soup.select(".tF2Cxc"):
        link = result.select_one(".yuRUbf a")["href"]
        links.append(link)

    if page_num == page_limit:
        break
    if soup.select_one(".d6cvqb a[id=pnnext]"):
        params["start"] += 10
    else:
        break

with open(output, "w") as file:
    for link in links:
        print(link, file=file)
