import requests
from bs4 import BeautifulSoup as bs
from langdetect import detect


class BBC:
    """
    Scraper for BBC articles.
    For the moment it extracts the title and content of an article given by URL.
    """
    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, 'html.parser')
        self.body = self.get_body()
        self.title = self.get_title()
        self.language = self.get_language()

    def get_body(self) -> list:
        article_elem = self.soup.find('article')
        body = article_elem.find_all('div', {'data-component': 'text-block'})
        content = []
        for div in body:
            content.append(
                div.find('div').find('p').text
            )
        return content

    def get_title(self) -> str:
        return self.soup.find('h1').text

    def get_language(self) -> str:
        try:
            return self.soup.find('html')['lang']
        except:
            return detect(self.title)

    def to_object(self):
        return {
            'source': 'bbc',
            'title': self.title,
            'body': self.body,
            'language': self.language
        }


if __name__ == '__main__':
    article = BBC('https://www.bbc.com/news/world-us-canada-56368328')
    print(article.to_object())
