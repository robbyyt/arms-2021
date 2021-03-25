import requests
from bs4 import BeautifulSoup as bs
from langdetect import detect


class Mediafax:
    """
    Scraper for Mediafax articles.
    For the moment it extracts the title and content of an article given by URL.
    """

    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, 'html.parser')
        self.body = self.get_body()
        self.title = self.get_title()
        self.language = self.get_language()
        self.author = self.get_author()
        self.date = self.get_date()

    def get_body(self) -> list:
        try:
            description = self.soup.find('p', {'class': 'chapeau'}).text
            content = [description]
        except:
            content = []

        text_ps = self.soup.find('div', {'id': 'article_text_content'}).find('div', {'class': 'just-article-content'}).find_all('p')
        for p in text_ps:
            text = p.text.lstrip().rstrip()
            if text:
                content.append(text)
        return content

    def get_title(self) -> str:
        return self.soup.find('h1').text.lstrip().rstrip()

    def get_language(self) -> str:
        try:
            return self.soup.find('html')['lang']
        except:
            return detect(self.title)

    def get_author(self) -> str:
        try:
            return self.soup.find('a', {'class': 'author_link'}).text.lstrip().rstrip()
        except:
            return 'unkwnown'

    def get_date(self) -> str:
        try:
            return self.soup.find('time')['datetime']
        except:
            return 'unknown'

    def to_object(self):
        return {
            'source': 'mediafax',
            'title': self.title,
            'body': self.body,
            'language': self.language,
            'date': self.date,
            'author': self.author
        }


if __name__ == '__main__':
    article = Mediafax('https://www.mediafax.ro/politic/motiunea-depusa-impotriva-ministrului-economiei-a-fost-respinsa-19961033')
    print(article.to_object())
