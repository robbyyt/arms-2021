from deep_translator import GoogleTranslator
import json


def get_article_body(article):
    if "ro" in article["language"]:
        return "".join(article["body"])
    else:
        translation = [GoogleTranslator(source='auto', target='en').translate(p) for p in article["body"]]
        return "".join(translation)


if __name__ == '__main__':
    with open('data.json', 'r', encoding="utf8") as f:
        data = json.load(f)

    corpus = list(map(get_article_body, data))

    with open('corpus.json', 'w', encoding='utf-8') as f:
        json.dump(corpus, f, ensure_ascii=False, indent=4)