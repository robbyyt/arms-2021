import requests
from bs4 import BeautifulSoup as bs
from langdetect import detect


class Reporteris:
    """
    Scraper for Reporteris articles.
    For the moment it extracts the title and content of an article given by URL.
    """

    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, 'html.parser')
        self.body = self.get_body()
        self.title = self.get_title()
        self.language = self.get_language()

    def get_body(self) -> list:
        description = self.soup.find('div', {'class': 'itemIntroText'}).find('h5').text
        content = [description]
        intro = self.soup.find('div', {'class': 'itemIntroText'}).find('p').text
        content.append(intro)
        text_ps = self.soup.find('div', {'class': 'itemFullText'}).find_all('p')
        for p in text_ps:
            text = p.text.lstrip().rstrip()
            if text:
                content.append(text)
        content.pop()
        return content

    def get_title(self) -> str:
        return self.soup.find('h2', {'class': 'itemTitle'}).text.lstrip().rstrip()

    def get_language(self) -> str:
        return detect(self.title)

    def to_object(self):
        return {
            'source': 'reporteris',
            'title': self.title,
            'body': self.body,
            'language': self.language
        }


if __name__ == '__main__':
    article = Reporteris('https://www.reporteris.ro/component/k2/item/105055-4-luni-de-formare-civic%C4%83-pentru-fiul-primarului-din-pa%C8%99cani-pentru-c%C4%83-i-a-dat-un-pumn-%C3%AEn-ochi-unui-coleg-de-%C8%99coal%C4%83.html')
    print(article.to_object())
