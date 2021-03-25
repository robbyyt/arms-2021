import requests
from bs4 import BeautifulSoup as bs
from langdetect import detect


class Newsro:
    """
    Scraper for Hotnews articles.
    For the moment it extracts the title and content of an article given by URL.
    """

    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, 'html.parser')
        self.body = self.get_body()
        self.title = self.get_title()
        self.language = self.get_language()

    def get_body(self) -> list:
        content = []
        text_divs = self.soup.find('div', {'id': 'articleContent'}).find_all('div')
        for div in text_divs:
            text = div.text.lstrip().rstrip()
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

    def to_object(self):
        return {
            'source': 'hotnews',
            'title': self.title,
            'body': self.body,
            'language': self.language
        }


if __name__ == '__main__':
    article = Newsro('https://www.hotnews.ro/stiri-international-24671737-rusia-rechemat-ambasadorul-rus-sua-pentru-consultari.htm')
    print(article.to_object())
