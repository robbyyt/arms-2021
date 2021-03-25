import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_risLinks():
    pagesToGet = 10
    upperFrame=[]
    links_list = []
    url = "https://www.reporteris.ro/component/k2/itemlist/search.html?searchword=george+floyd&x=0&y=0&categories=&format=html&t=1616501273080&tpl=search"
    try:
        page = requests.get(url)
    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()  # get the exception information
        print('ERROR FOR LINK:', url)  # print the link that cause the problem
        print(error_type, 'Line:', error_info.tb_lineno)  # print error info and line that threw the exception
    # time.sleep(2)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('div', attrs={'class': 'genericItemView'})
    # print(len(links))
    for j in links:
        Link = j.find('h2', attrs={'class': 'genericItemTitle'}).find('a')['href'].strip()
        links_list.append("https://www.reporteris.ro"+Link)


    return(links_list)