import requests
# pip install requests
response=requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(input("Enter City Name: "),"4ca552e9eb5fce4ad6da46483e5da915"))
data=response.json()
for (key,value) in data.items():
    print(key,value)
print(data["main"]["temp"])