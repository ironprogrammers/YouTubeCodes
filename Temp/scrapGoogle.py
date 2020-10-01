from bs4 import BeautifulSoup
import requests
import re
#import urllib2
import urllib.request as urllib2
import os
#import cookielib
import http.cookiejar as cookielib
import json

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')


query = input("query image=")# you can change the query for the image  here
image_type="ActiOn"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print (url)
#add the directory for your image here
DIR="/home/the-wolf/Downloads/tp_download"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)
#print(soup)

ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("img",{"class":"rg_i Q4LuWd"}):
    print("Hi",a["src"])
    # link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    # ActualImages.append((link,Type))

print("there are total" , len(ActualImages),"images")