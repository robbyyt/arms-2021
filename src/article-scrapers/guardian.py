import requests
from bs4 import BeautifulSoup as bs
from langdetect import detect


class Guardian:
    """
    Scraper for Guardian articles.
    For the moment it extracts the title and content of an article given by URL.
    """

    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, 'html.parser')
        self.body = self.get_body()
        self.title = self.get_title()
        self.language = self.get_language()

    def get_body(self) -> list:
        description = self.soup.find('div', {'class': 'css-xmt4aq'}).find('p').text
        content = [description]
        text_ps = self.soup.find('div', {'class': 'article-body-commercial-selector'}).find_all('p')
        for p in text_ps:
            content.append(p.text)
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
            'title': self.title,
            'body': self.body,
            'language': self.language
        }


if __name__ == '__main__':
    article = Guardian('https://www.theguardian.com/world/2021/mar/16/israeli-archeologists-find-new-dead-sea-scroll-fragments')
    print(article.to_object())
