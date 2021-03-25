import sys
import traceback
import json

from articlescrapers.bbc import BBC
from articlescrapers.aljazeera import Aljazeera
from articlescrapers.cnn import CNN
from articlescrapers.guardian import Guardian
from articlescrapers.hotnews import Hotnews
from articlescrapers.libertatea import Libertatea
from articlescrapers.mediafax import Mediafax
from articlescrapers.newsro import Newsro
from articlescrapers.politico import Politico
from articlescrapers.reporteris import Reporteris
from articlescrapers.theeconomist import Economist

from articlelinks.bbc import get_bbcLinks
from articlelinks.aljazeera import get_aljLinks
from articlelinks.guardian import get_gdnLinks
from articlelinks.hotnews import get_hotnwsLinks
from articlelinks.libertatea import get_lbrLinks
from articlelinks.mediafax import get_mfLinks
from articlelinks.newsro import get_nwsLinks
from articlelinks.reporteris import get_risLinks
from articlelinks.tv5monde import get_tv5Links

cnn_links = ['https://edition.cnn.com/2021/03/10/us/derek-chauvin-trial-jurors/index.html','https://edition.cnn.com/2021/03/19/us/pew-research-data-race-discrimination-trnd/index.html','https://edition.cnn.com/2021/03/14/us/minneapolis-george-floyd-square-battleground-soh/index.html','https://edition.cnn.com/2021/03/12/us/george-floyd-minneapolis-settlement/index.html','https://edition.cnn.com/2021/03/11/us/derek-chauvin-george-floyd-charges/index.html','https://edition.cnn.com/2021/03/08/us/derek-chauvin-trial-jury/index.html','https://edition.cnn.com/videos/justice/2021/03/11/derek-chauvin-third-degree-charge-honig-nr-vpx.cnn','https://edition.cnn.com/2021/03/08/us/race-relations-george-floyd-poll/index.html']
# tv5_links = ['https://information.tv5monde.com/video/etats-unis-la-famille-de-george-floyd-recoit-27-millions-de-dollars-de-dedommagement','https://information.tv5monde.com/video/qui-etait-george-floyd-cet-homme-devenu-un-symbole-des-violences-policieres','https://information.tv5monde.com/info/france-les-violences-policieres-en-debat-du-deni-la-crise-385468','https://information.tv5monde.com/video/etats-unis-derek-chauvin-le-policier-accuse-d-avoir-tue-george-floyd-libere-sous-caution','https://information.tv5monde.com/video/en-afrique-les-reactions-la-mort-de-george-floyd','https://information.tv5monde.com/info/george-floyd-le-destin-tragique-d-un-homme-devenu-l-incarnation-de-la-lutte-antiraciste-399404','https://information.tv5monde.com/video/mort-de-george-floyd-et-hardel-sherrell-aux-etats-unis-minneapolis-la-colere-ne-retombe-pas','https://information.tv5monde.com/info/le-jury-quasi-constitue-au-proces-du-meurtre-de-george-floyd-401551','https://information.tv5monde.com/video/etats-unis-comment-reconstruire-un-monde-plus-juste-apres-la-mort-de-george-floyd','https://information.tv5monde.com/video/george-floyd-symbole-mondial-du-racisme-et-des-violences-policieres','https://information.tv5monde.com/video/mort-de-george-floyd-symboles-et-monuments-en-ligne-de-mire','https://information.tv5monde.com/video/mort-de-george-floyd-heurts-et-feux-devant-la-maison-blanche','https://information.tv5monde.com/video/mort-de-george-floyd-aux-etats-unis-les-transformations-pour-mettre-fin-au-racisme-seront']


if __name__ == '__main__':
    articles = []

    current_articles = get_bbcLinks()
    for article in current_articles:
        if 'programmes' not in article:
            try:
                articles.append(BBC(article).to_object())
            except:
                print("Article: %s cannot be converted to object" % article)

    current_articles = get_aljLinks()
    for article in current_articles:
        try:
            articles.append(Aljazeera(article).to_object())
        except:
            print("Article: %s cannot be converted to object" % article)

    # TODO: MAKE IT FETCH MORE ARTICLES
    current_articles = get_gdnLinks()
    for article in current_articles:
        try:
            articles.append(Guardian(article).to_object())
        except Exception as e:
            print("Article: %s cannot be converted to object" % article)
            # traceback.print_exc()

    current_articles = get_hotnwsLinks()
    for article in current_articles:
        try:
            articles.append(Hotnews(article).to_object())
        except Exception as e:
            print("Article: %s cannot be converted to object" % article)
            # traceback.print_exc()

    current_articles = get_lbrLinks()
    print(current_articles)
    print(len(current_articles))
    for article in current_articles:
        try:
            articles.append(Libertatea(article).to_object())
        except Exception as e:
            print("Article: %s cannot be converted to object" % article)
            # traceback.print_exc()

    current_articles = get_mfLinks()
    for article in current_articles:
        try:
            articles.append(Mediafax(article).to_object())
        except Exception as e:
            print("Article: %s cannot be converted to object" % article)
            # traceback.print_exc()


    current_articles = get_nwsLinks()
    for article in current_articles:
        try:
            articles.append(Newsro(article).to_object())
        except Exception as e:
            print("Article: %s cannot be converted to object" % article)
            # traceback.print_exc()

    current_articles = get_risLinks()
    for article in current_articles:
        try:
            articles.append(Reporteris(article).to_object())
        except Exception as e:
            print("Article: %s cannot be converted to object" % article)
            # traceback.print_exc()

    for article in cnn_links:
        try:
            articles.append(CNN(article).to_object())
        except Exception as e:
            print("Article: %s cannot be converted to object" % article)
            # traceback.print_exc()

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
