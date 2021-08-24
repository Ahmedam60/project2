import csv

import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"

page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
print(soup.title.string)
bs_titles = soup.findAll("a",class_="gem-c-document-list__item-title")
titles = []
for title in bs_titles:
    titles.append(title.string)

#print(titles)

bs_desc = soup.findAll('p',class_="gem-c-document-list__item-description")
description = []
for desc in bs_desc:
    description.append(desc.string)

#print(description)
dic = dict(zip(titles,description))

#print(dic)
header = ["Titles","Description"]

with open(r"D:\ALGO\Finance\data1.csv","w",encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter =",")
    writer.writerow(header)

    for i in range(len(titles)):
        row = [titles[i], description[i]]
        #writer.writerow(row)
        writer.writerows([row])