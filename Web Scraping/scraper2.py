URL="https://en.wikipedia.org/wiki/" # const
# pip install bs4 , requests
from bs4 import BeautifulSoup
import requests
search=input("Enter The search")
URL+=search
print(URL)
response=requests.get(URL)
data=BeautifulSoup(response.content,"html5lib")
# print(data.findAll("p")[10].text)
def parser(listA):
    res=""
    for each in listA:
        res+=each.text
    return "\n".join(res.split("."))
result=parser(data.findAll("p"))
with open("result.txt","w",encoding="utf-8") as file:
    file.write(result)
