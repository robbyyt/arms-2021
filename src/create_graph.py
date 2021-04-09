import networkx as nx
import json
import math
import random
from sklearn.feature_extraction.text import TfidfVectorizer


def convert_index(corpus_normalized_index, corpus):
    index = 0
    for i in range(len(corpus)):
        if corpus[i]:
            if index == corpus_normalized_index:
                return index
            else:
                index += 1


def construct_index_correspondence(corpus_normalized, corpus):
    indexes = []
    for i in range(len(corpus_normalized)):
        indexes.append(corpus.index(corpus_normalized[i]))
    return indexes


def construct_graph(corpus, sim_matrix, data, corpus_normalized):
    indexes = construct_index_correspondence(corpus_normalized, corpus)
    cmin = 0
    cmax = 1
    G = nx.Graph()
    source_colors = {}
    for i in range(len(sim_matrix)):
        for j in range(len(sim_matrix[0])):
            if i != j and sim_matrix[i][j] >= 0.25:

                if data[indexes[i]]["source"] not in source_colors:
                    r, g, b = rgb(random.uniform(cmin, cmax), cmin, cmax)
                    source_colors[data[indexes[i]]["source"]] = {'color': {'r': r, 'g': g, 'b': b, 'a': 0}}

                if data[indexes[j]]["source"] not in source_colors:
                    r, g, b = rgb(random.uniform(cmin, cmax), cmin, cmax)
                    source_colors[data[indexes[j]]["source"]] = {'color': {'r': r, 'g': g, 'b': b, 'a': 0}}

                G.add_node(data[indexes[i]]["source"] + " " + data[indexes[i]]["title"], viz=source_colors[data[indexes[i]]["source"]])
                G.add_node(data[indexes[j]]["source"] + " " + data[indexes[j]]["title"], viz=source_colors[data[indexes[j]]["source"]])
                # r, g, b = rgb(sim_matrix[i][j], cmin, cmax)
                # color = {'color': {'r': r, 'g': g, 'b': b, 'a': 0}}
                G.add_edge(data[indexes[i]]["source"] + " : " + data[indexes[i]]["title"],
                           data[indexes[j]]["source"] + " : " + data[indexes[j]]["title"], weight=sim_matrix[i][j])

    return G


def floatRgb(mag, cmin, cmax):
    """ Return a tuple of floats between 0 and 1 for R, G, and B. """
    # Normalize to 0-1
    try: x = float(mag-cmin)/(cmax-cmin)
    except ZeroDivisionError: x = 0.5 # cmax == cmin
    blue  = min((max((4*(0.75-x), 0.)), 1.))
    red   = min((max((4*(x-0.25), 0.)), 1.))
    green = min((max((4*math.fabs(x-0.5)-1., 0.)), 1.))
    return red, green, blue


def rgb(mag, cmin, cmax):
    """ Return a tuple of integers, as used in AWT/Java plots. """
    red, green, blue = floatRgb(mag, cmin, cmax)
    return int(red*255), int(green*255), int(blue*255)


def strRgb(mag, cmin, cmax):
    """ Return a hex string, as used in Tk plots. """
    return "#%02x%02x%02x" % rgb(mag, cmin, cmax)


if __name__ == '__main__':
    with open('data.json', 'r', encoding="utf8") as f:
        data = json.load(f)

    with open('corpus_en.json', 'r', encoding="utf8") as f:
        corpus = json.load(f)

    corpus_normalized = [i for i in corpus if i]
    ro_sw =frozenset(["a","abia","acea","aceasta","această","aceea","aceeasi","acei","aceia","acel","acela","acelasi","acele","acelea","acest","acesta","aceste","acestea","acestei","acestia","acestui","aceşti","aceştia","acolo","acord","acum","adica","ai","aia","aibă","aici","aiurea","al","ala","alaturi","ale","alea","alt","alta","altceva","altcineva","alte","altfel","alti","altii","altul","am","anume","apoi","ar","are","as","asa","asemenea","asta","astazi","astea","astfel","astăzi","asupra","atare","atat","atata","atatea","atatia","ati","atit","atita","atitea","atitia","atunci","au","avea","avem","aveţi","avut","azi","aş","aşadar","aţi","b","ba","bine","bucur","bună","c","ca","cam","cand","capat","care","careia","carora","caruia","cat","catre","caut","ce","cea","ceea","cei","ceilalti","cel","cele","celor","ceva","chiar","ci","cinci","cind","cine","cineva","cit","cita","cite","citeva","citi","citiva","conform","contra","cu","cui","cum","cumva","curând","curînd","când","cât","câte","câtva","câţi","cînd","cît","cîte","cîtva","cîţi","că","căci","cărei","căror","cărui","către","d","da","daca","dacă","dar","dat","datorită","dată","dau","de","deasupra","deci","decit","degraba","deja","deoarece","departe","desi","despre","deşi","din","dinaintea","dintr","dintr-","dintre","doar","doi","doilea","două","drept","dupa","după","dă","e","ea","ei","el","ele","era","eram","este","eu","exact","eşti","f","face","fara","fata","fel","fi","fie","fiecare","fii","fim","fiu","fiţi","foarte","fost","frumos","fără","g","geaba","graţie","h","halbă","i","ia","iar","ieri","ii","il","imi","in","inainte","inapoi","inca","incit","insa","intr","intre","isi","iti","j","k","l","la","le","li","lor","lui","lângă","lîngă","m","ma","mai","mare","mea","mei","mele","mereu","meu","mi","mie","mine","mod","mult","multa","multe","multi","multă","mulţi","mulţumesc","mâine","mîine","mă","n","ne","nevoie","ni","nici","niciodata","nicăieri","nimeni","nimeri","nimic","niste","nişte","noastre","noastră","noi","noroc","nostri","nostru","nou","noua","nouă","noştri","nu","numai","o","opt","or","ori","oricare","orice","oricine","oricum","oricând","oricât","oricînd","oricît","oriunde","p","pai","parca","patra","patru","patrulea","pe","pentru","peste","pic","pina","plus","poate","pot","prea","prima","primul","prin","printr-","putini","puţin","puţina","puţină","până","pînă","r","rog","s","sa","sa-mi","sa-ti","sai","sale","sau","se","si","sint","sintem","spate","spre","sub","sunt","suntem","sunteţi","sus","sută","sînt","sîntem","sînteţi","să","săi","său","t","ta","tale","te","ti","timp","tine","toata","toate","toată","tocmai","tot","toti","totul","totusi","totuşi","toţi","trei","treia","treilea","tu","tuturor","tăi","tău","u","ul","ului","un","una","unde","undeva","unei","uneia","unele","uneori","unii","unor","unora","unu","unui","unuia","unul","v","va","vi","voastre","voastră","voi","vom","vor","vostru","vouă","voştri","vreme","vreo","vreun","vă","x","z","zece","zero","zi","zice","îi","îl","îmi","împotriva","în","înainte","înaintea","încotro","încât","încît","între","întrucât","întrucît","îţi","ăla","ălea","ăsta","ăstea","ăştia","şapte","şase","şi","ştiu","ţi","ţie"])
    vect = TfidfVectorizer(min_df=1, stop_words="english")
    tfidf = vect.fit_transform(corpus_normalized)
    pairwise_sim = tfidf * tfidf.T
    sim_matrix = pairwise_sim.A
    G = construct_graph(corpus, sim_matrix, data, corpus_normalized)
    color_map = []
    # nx.draw(G)
    # plt.savefig("graph_en.png")
    nx.write_gexf(G, 'graph_en.gexf')