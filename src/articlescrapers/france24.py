import requests
from bs4 import BeautifulSoup as bs
from langdetect import detect


class France24:
    """
    Scraper for France24 articles.
    For the moment it extracts the title and content of an article given by URL.
    """

    def __init__(self, url: str):
        article = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'})
        self.soup = bs(article.content, 'html.parser')
        self.body = self.get_body()
        self.title = self.get_title()
        self.language = self.get_language()
        self.author = self.get_author()
        self.date = self.get_date()

    def get_body(self) -> list:
        description = self.soup.find('p', {'class': 't-content__chapo'}).text.lstrip().rstrip()
        content = [description]
        text_ps = self.soup.find('div', {'class': 't-content__body'}).find_all('p')
        for p in text_ps:
            content.append(p.text.lstrip().rstrip())

        content.pop()
        content.pop()
        if content[len(content) - 1] == '(AP)':
            content.pop()

        return content

    def get_title(self) -> str:
        return self.soup.find('h1').text

    def get_language(self) -> str:
        try:
            return self.soup.find('html')['lang']
        except:
            return detect(self.title)

    def get_author(self) -> str:
        try:
            return self.soup.find('span', {'class': 'itemAuthor'}).find('a').text.lstrip()
        except:
            return 'unkwnown'

    def get_date(self) -> str:
        try:
            return self.soup.find('time')['datetime']
        except:
            return 'unknown'

    def to_object(self):
        return {
            'source': 'france24',
            'title': self.title,
            'body': self.body,
            'language': self.language,
            'date': self.date,
            'author': self.author
        }


if __name__ == '__main__':
    article = France24('https://www.france24.com/en/middle-east/20210320-turkey-quits-landmark-istanbul-convention-protecting-women-from-violence')
    print(article.to_object())
