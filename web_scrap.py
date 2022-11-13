import requests
from bs4 import BeautifulSoup
from lxml import etree

#Get Request
r=requests.get("https://deadline.com/2022/09/constantine-sequel-keanu-reeves-francis-lawrence-warner-bros-dc-akiva-goldsman-scripting-producing-bad-robot-jj-abrams-hannah-minghella-1235121127/")


#print website url
print(r.url)
# check status code for response received
# success code - 200
print(r.status_code)

#print content of request
#print(r.content)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())

print(soup.title)
dom = etree.HTML(str(soup))
print(dom.xpath('//*[@id="post-1235121127"]/div[2]/article/div[1]/p[1]')[0].text) 
print(dom.xpath('//*[@id="post-1235121127"]/div[2]/article/div[1]/p[2]')[0].text) 

print(dom.xpath('//*[@id="post-1235121127"]/div[2]/article/div[1]/p[5]')[0].text) 
print(dom.xpath('//*[@id="post-1235121127"]/div[2]/article/div[1]/p[6]')[0].text) 

print(dom.xpath('//*[@id="post-1235121127"]/div[2]/article/div[1]/p[8]')[0].text) 
print(dom.xpath('//*[@id="post-1235121127"]/div[2]/article/div[1]/p[9]')[0].text) 
