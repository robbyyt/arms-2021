import requests
from bs4 import BeautifulSoup as bs
from langdetect import detect


class CNN:
    """
    Scraper for CNN articles.
    For the moment it extracts the title and content of an article given by URL.
    """
    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, 'html.parser')
        self.body = self.get_body()
        self.title = self.get_title()
        self.language = self.get_language()

    def get_body(self) -> list:
        description = self.soup.find_all('p', {'class': 'zn-body__paragraph'})
        description_text = ''
        for tag in description:
            description_text += tag.text
        content = [description_text]
        text_divs = self.soup.find_all('div', {'class': 'zn-body__paragraph'})

        for div in text_divs:
            content.append(div.text)

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
            'source': 'cnn',
            'title': self.title,
            'body': self.body,
            'language': self.language
        }


if __name__ == '__main__':
    article = CNN('https://edition.cnn.com/2021/03/11/americas/brazil-variants-simultaneous-infection-intl/index.html')
    print(article.to_object())