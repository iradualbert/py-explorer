import requests
data = requests.get("http://ipinfo.io/169.7.147.0/json")
print(data.json())
print(data.text)