import requests
from bs4 import BeautifulSoup as bs
from langdetect import detect


class Politico:
    """
    Scraper for Politico articles.
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
        description = self.soup.find('p', {'class': 'dek'}).text
        content = [description]
        text_ps = self.soup.find_all('p', {'class': 'story-text__paragraph'})
        for p in text_ps:
            content.append(p.text)
        return content
    
    def get_title(self) -> str:
        return self.soup.find('h2', {'class': 'headline'}).text

    def get_language(self) -> str:
        try:
            return self.soup.find('html')['lang']
        except:
            return detect(self.title)

    def get_author(self) -> str:
        try:
            return self.soup.find('p', {'class': 'story-meta__authors'}).text.lstrip()
        except:
            return 'unkwnown'

    def get_date(self) -> str:
        try:
            return self.soup.find('time')['datetime']
        except:
            return 'unknown'

    def to_object(self):
        return {
            'source': 'politico',
            'title': self.title,
            'body': self.body,
            'language': self.language,
            'date': self.date,
            'author': self.author
        }


if __name__ == '__main__':
    article = Politico('https://www.politico.com/news/2021/03/12/cuomo-ny-congress-democrats-resignations-475522')
    print(article.to_object())
