import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=5e8b7a9e06e74a219d71a000d8484dca')
response = requests.get(url)
resp= (response.json())
#print(resp)
# getting heading from dict.
news_heading=(resp['articles'])
for i in news_heading:
	print(i['title'],'\n')