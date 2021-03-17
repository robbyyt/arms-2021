import requests
from bs4 import BeautifulSoup as bs
from langdetect import detect


class Economist:
    """
    Scraper for Economist articles.
    For the moment it extracts the title and content of an article given by URL.
    """

    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, 'html.parser')
        self.body = self.get_body()
        self.title = self.get_title()
        self.language = self.get_language()

    def get_body(self) -> list:
        description = self.soup.find('p', {'class': 'article__description'}).text
        content = [description]
        text_ps = self.soup.find_all('p', {'class': 'article__body-text'})
        for p in text_ps:
            content.append(p.text)

        return content

    def get_title(self) -> str:
        return self.soup.find('span', {'class': 'article__headline'}).text

    def get_language(self) -> str:
        try:
            return self.soup.find('html')['lang']
        except:
            return detect(self.title)

    def to_object(self):
        return {
            'source': 'economist',
            'title': self.title,
            'body': self.body,
            'language': self.language
        }


if __name__ == '__main__':
    article = Economist('https://www.economist.com/science-and-technology/2021/03/15/eu-countries-pause-astrazenecas-covid-19-jab-over-safety-fears')
    print(article.to_object())
