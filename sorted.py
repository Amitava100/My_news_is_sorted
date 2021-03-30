import requests
from bs4 import BeautifulSoup
import pprint

response1=requests.get('https://news.ycombinator.com/')
response2=requests.get('https://news.ycombinator.com/news?p=2')

soup1=BeautifulSoup(response1.text,'html.parser')
soup2=BeautifulSoup(response2.text,'html.parser')

links1=soup1.select('.storylink')
links2=soup2.select('.storylink')

subtext1=soup1.select('.subtext')
subtext2=soup2.select('.subtext')

mega_links=links1+links2
mega_subtext=subtext1+subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key=lambda k:k['votes'],reverse=True)

def create_yourown_hn(links,subtext):
	hn=[]
	for index,items in enumerate(links):
		title=items.getText()
		href=items.get('href',None)
		vote=subtext[index].select('.score')
		if len(vote):
			points=int(vote[0].getText().replace('points',''))
			if points>99:
				hn.append({'title':title,'link':href,'votes':points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_yourown_hn(mega_links,mega_subtext))
