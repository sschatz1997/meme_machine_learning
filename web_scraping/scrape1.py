# scrape1.py
import re
import sys
import json
import config
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from unidecode import unidecode
# https://realpython.com/beautiful-soup-web-scraper-python/

def remove_non_ascii(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])


def getNameObj():
    if sys.platform == "win32":
        path = config.windowPathJSON
    elif sys.platform == "linux":
        path = config.linuxPathJSON
    f1 = path + "names.json"

    with open(f1) as f:
        data = json.load(f)
    f.close()

    return data

def writeNameObj(data):
    if sys.platform == "win32":
        path = config.windowPathJSON
    elif sys.platform == "linux":
        path = config.linuxPathJSON
    file1 = path + "names.json"
    
    with open(file1, "w") as f1:
        json.dump(data, f1, sort_keys=False, indent=4)
    f1.close()

def pull1():
    URL = "https://www.thrillist.com/entertainment/nation/best-memes-of-all-time"
    ML = []
    page = requests.get(URL)
    data = getNameObj()

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="main-content")
    #print(results.prettify())

    tests = results.find_all('h2')
    for test in tests:
        #print(test.text)
        temp = test.text
        temp2 = temp.split(".")
        #print(temp2[1])
        ML.append(temp2)

    x = 0
    while(x != len(ML)):
        data["names"].append(remove_non_ascii(ML[x][1]))
        print(remove_non_ascii(ML[x][1]))
        x += 1

    writeNameObj(data)

"""
for classT1 in classT1s:
    #print(classT1, end="\n"*2)
    elm1 = classT1.find('h2', class_="styles__BodyText-d07mme-0")
    prin
"""

def pull2():
    URL = "https://www.thrillist.com/entertainment/nation/best-memes-of-all-time"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="main-content")
    #print(results.prettify())

    tests = results.find_all('img')
    for test in tests:
        t2s = test.find_all("data-src", string="http")
        print(t2s)
        #print(test)

    """
    #print(results.prettify())
    links = results.find_all('div', {'class': 'img--no-scale lazyloaded'})
    for link in links:
        print(link.find('img')['src'])
        print(link.find('img')['title'])
    tests = results.find_all('img', class_="img--no-scale")
    for test in tests:
        x = test.find("src")
        print(x)
    """

def pull4():
    URL = "https://www.liveabout.com/internet-memes-that-have-won-our-hearts-3573553"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="main")
    data = getNameObj()
    
    tests = results.find_all('h2')

    for test in tests:
        print(test.text)
        data["names"].append(test.text)

    writeNameObj(data)

def pull5():
    URL = "https://qz.com/1296094/most-popular-memes-finally-a-scientific-list-of-the-most-popular-memes-on-the-internet/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="root")
    data = getNameObj()
    tests = results.find_all('td')

    for test in tests:
        print(test.text)
        data["names"].append(remove_non_ascii(test.text))

    writeNameObj(data)

def pull6():
    URL = "https://www.buzzfeednews.com/article/katienotopoulos/memes-that-defined-the-2010s"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="news-content")
    data = getNameObj()
    tests = results.find_all('span', class_='js-subbuzz__title-text')

    for test in tests:
        print(test.text)
        data["names"].append(remove_non_ascii(test.text))

    writeNameObj(data)

pull6()