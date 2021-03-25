import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_tv5Links():
    pagesToGet = 1
    upperFrame=[]
    links_list = []
    for page in range(1,pagesToGet+1):
        url="https://information.tv5monde.com/search/site/george%20floyd?page="+str(page)
        try:
            page=requests.get(url)
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()  # get the exception information
            print('ERROR FOR LINK:', url)  # print the link that cause the problem
            print(error_type, 'Line:', error_info.tb_lineno)  # print error info and line that threw the exception
            continue
        #time.sleep(2)
        soup=BeautifulSoup(page.text,'html.parser')
        links=soup.find_all('div',attrs={'class':'field-items'})
        #print(len(links))
        for j in links:
            Link = j.find('h2')
            if Link is not None:
                Link=Link.find('a')['href'].strip()
                links_list.append("https://information.tv5monde.com"+Link)


    return(links_list)
