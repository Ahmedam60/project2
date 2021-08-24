## CREATED AT 24-AUG-2021 ##
#AUTHOR:AHMED AMIN#

#USED LIBRARY (BEUTIFULSOUP,REQUESTS AND CSV)


import requests
from bs4 import BeautifulSoup
import csv

#FUNCTION TO CONVERT ELEMENTS TO STRING ELEMENTS
def convert_string(elements):
    item = []
    for i in elements:
        item.append(i.string)

    return item

#FUNCTION TO CREATE AND STORE DATA INTO FILE
def load_data(file,header,titles,description):
    with open(r"D:\ALGO\Finance\data2.csv", "w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(header)

        for i in range(len(titles)):
            row = [titles[i], description[i]]
            writer.writerows([row])


def main():

    #URL TO SCRAPE
    url = "https://www.gov.uk/search/news-and-communications"
    page = requests.get(url)

    #CREATE BEUTIFULSOUP OBJECT
    soup = BeautifulSoup(page.content,'html.parser')

    #GET ALL TITLES WITH SPECIFIC CLASS
    titles = soup.findAll('a', class_='gem-c-document-list__item-title')
#    #GET ALL DESCRIPTION WITH SPECIFIC CLASS
    description = soup.findAll('p', class_='gem-c-document-list__item-description')
    header = ['Titles' ,'Description']
    titles = convert_string(titles)
    description = convert_string(description)
    load_data(r"D:\ALGO\Finance\data2.csv", header , titles , description)

main()