import urllib.request
import ssl
import re
import requests 
from bs4 import BeautifulSoup  
from distutils.filelist import findall  
import pprint
import json
import time
class GetUrl:
  def __init__(self,repo_url) : 
    self.repo_url = repo_url
    self.getPage(repo_url)

  def getPage(self,repo_url):
    repo_url+='/search?p={page}&q=http'
    htmls=[]
    urls=[]
    page = urllib.request.urlopen(repo_url)   
    contents = page.read()
    soup = BeautifulSoup(contents,"html.parser") 
    page=soup.find('em')
    if page != None :
      totalPage =int(soup.em['data-total-pages'])
      for idx in range (totalPage):
        r = requests.get(repo_url.format(page=idx+1))
        html= r.text
        htmls.append(html)
        url_page = self.parseSingleHtml(html)
        if len(url_page) :
          for url in url_page:
            urls.append(url)
        #time.sleep(3)
    else:
      r = requests.get(repo_url)
      html= r.text
      htmls.append(html)
      if len(self.parseSingleHtml(html)) :
        urls.append(self.parseSingleHtml(html))
    urls = list(set(urls))
    return urls

  @staticmethod
  def parseSingleHtml(html):
      datas = []
      soup = BeautifulSoup(html,'html.parser')
      innerHtml = str(soup.find_all('td',class_= 'blob-code blob-code-inner'))
      dd = re.sub(r'</?\w+[^>]*>','',innerHtml)
      url = re.findall('[\'"]?([^\'" >]+)', dd)
      for val in url:
        if "http://"in val :
          val = 'http'+val.split('http')[-1]
          datas.append(val)
      datas = list(set(datas))
      return datas


