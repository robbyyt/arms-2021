import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_gdnLinks():
    pagesToGet = 10
    upperFrame=[]
    links_list = []
    for page in range(2, pagesToGet + 1):
        url = "https://www.france24.com/en/tag/george-floyd/"+str(page)+"/#pager"
        try:
            page = requests.get(url)
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()  # get the exception information
            print('ERROR FOR LINK:', url)  # print the link that cause the problem
            print(error_type, 'Line:', error_info.tb_lineno)  # print error info and line that threw the exception
        # time.sleep(2)
        soup = BeautifulSoup(page.text, 'html.parser')
        links = soup.find_all('div', attrs={'class': 'o-layout-list__item 1-m-100 1-t-50 l-d-33'})
        # print(len(links))
        for j in links:
            Link = j.find("div", attrs={'class': 'm-item-list-article'}).find('a')['href'].strip()
            links_list.append(Link)

        return (links_list)
