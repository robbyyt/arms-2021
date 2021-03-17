import requests
from bs4 import BeautifulSoup as bs
from langdetect import detect


class Libertatea:
    """
    Scraper for Libertatea articles.
    For the moment it extracts the title and content of an article given by URL.
    """

    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, 'html.parser')
        self.body = self.get_body()
        self.title = self.get_title()
        self.language = self.get_language()

    def get_body(self) -> list:
        description = self.soup.find('p', {'class': 'intro'}).text.lstrip()
        content = [description]
        text_ps = self.soup.find('div', {'class': 'article-body'}).find_all('p')
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

    def to_object(self):
        return {
            'source': 'libertatea',
            'title': self.title,
            'body': self.body,
            'language': self.language
        }


if __name__ == '__main__':
    article = Libertatea('https://www.libertatea.ro/stiri/tvr-pierde-procesul-cu-libertatea-intentat-dupa-dezvaluirile-ziarului-despre-cheltuielile-de-aproape-jumatate-de-milion-de-euro-cu-eurovisionul-3456545')
    print(article.to_object())
