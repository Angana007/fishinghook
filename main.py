import requests
from bs4 import BeautifulSoup
import urllib2

# webpage = raw_input("Enter your link here: ")  ####For others' convenience
# source = urllib2.urlopen(webpage)
source = requests.get("https://arxiv.org/list/astro-ph.HE/recent").text #my field of interest
soup=BeautifulSoup(source, 'lxml')
targets = []
for a in soup.find_all("div", class_="list-title mathjax"):
    target = a.text
    targets.append(target)
    
subs = input("Enter your value: ") #######need to modify code so that lower case and upper case doesn't matter anymore
res = [i for i in targets if subs in i]
print(res)
