from bs4 import BeautifulSoup
import urllib3
import pandas as pd 
def extractUrls():
  urllib3.disable_warnings()
http = urllib3.PoolManager()
url_list = []
userInp = input("please enter url:")
print("user entered url is:",userInp)
response = http.request('GET', userInp,headers={'Accept-Encoding': 'br'})
soup =BeautifulSoup(response.data.decode('utf-8'),"lxml")
for links in soup.find_all("a"):
	url_list.append(links.get("href"))
df=pd.DataFrame(url_list,columns=["urls"])
print(df)
