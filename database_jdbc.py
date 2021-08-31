import urllib.request
import re
import requests 
from bs4 import BeautifulSoup  
from distutils.filelist import findall  

#module pour détecter base de donnés en utilisant le mot-clé 'jdbc'

def getPage(url):
  url+='/search?p={page}&q=jdbc'
  htmls=[]
  databases=[]
  page = urllib.request.urlopen(url)   
  contents = page.read()
  soup = BeautifulSoup(contents,"html.parser") 
  page=soup.find('em')
  if page != None :
    totalPage =int(soup.em['data-total-pages'])
    for idx in range (totalPage):
      r = requests.get(url.format(page=idx+1))
      html= r.text
      htmls.append(html)
      if len(parseSingleHtml(html)) :
        for val in parseSingleHtml(html):
          databases.append(val)
    databases = list(set(databases))
      #time.sleep(3)
  else:
    r = requests.get(url)
    html= r.text
    htmls.append(html)
    if len(parseSingleHtml(html)) :
      for val in parseSingleHtml(html):
        databases.append(val)
    databases = list(set(databases))
  print(databases)
  return databases

def parseSingleHtml(html):
    datas = []
    soup = BeautifulSoup(html,'html.parser')
    innerHtml = str(soup.find_all('td',class_= 'blob-code blob-code-inner'))
    dd = re.sub(r'</?\w+[^>]*>','',innerHtml)
    database = re.findall('[\'"]?([^\'" >]+)', dd)
    for val in database:
      if "jdbc:" in val :
        if '/' in val:
          datas.append(val.split('/')[-1])  
    return datas

url="https://github.com/microservices-patterns/ftgo-application"
#url='https://github.com/Microservice-API-Patterns/LakesideMutual'
#url = "https://github.com/FudanSELab/train-ticket"
#url ='https://github.com/JoeCao/qbike'
databases=getPage(url)

