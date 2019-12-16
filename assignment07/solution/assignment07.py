
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


# Create list for each level with '0' as root page

pageslevel0 = ["/wiki/Wikipedia:Hauptseite"]
pageslevel1 = []
pageslevel2 = []


html = urlopen("https://de.wikipedia.org/wiki/Wikipedia:Hauptseite")
bsObj = BeautifulSoup(html, "html.parser") # create soup object for root page

for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")): # regex
    #  looking for internal articles
    if 'href' in link.attrs:
        newPage = link.attrs['href']
        if newPage not in pageslevel1 and newPage not in pageslevel0:  # check to see if page already extracted
            pageslevel1.append(newPage) # list of links found on root page


for newPage in pageslevel1:
    soup2 = BeautifulSoup(urlopen("https://de.wikipedia.org" + newPage), "html.parser")  # create soup obj for each new
    # link
    for link in soup2.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            page2 = link.attrs['href']
            if page2 not in pageslevel2 and page2 not in pageslevel1 and page2 not in pageslevel0:
                pageslevel2.append(page2) # after checking if the link has already been captured, new links added
                # as level 2 links
print(len(pageslevel2))
print(len(pageslevel1))

import csv
#  Creating list of lists containing each link and lowest level of that link
links_csv = [["Level", "link_URL"], [0, "https://de.wikipedia.org/wiki/Wikipedia:Hauptseite"]] # headers and root level
for page in pageslevel1:
    links_csv.append([1, "https://de.wikipedia.org/" + page])
for page in pageslevel2:
    links_csv.append([2, "https://de.wikipedia.org/" + page])

with open("links.csv", "w", newline='') as file: # creating csvfile
    writer = csv.writer(file)
    writer.writerows(links_csv)

