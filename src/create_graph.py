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
            if i != j and sim_matrix[i][j] >= 0.25 and data[indexes[i]]["source"] != data[indexes[j]]["source"]:

                if data[indexes[i]]["source"] not in source_colors:
                    source_colors[data[indexes[i]]["source"]] = strRgb(random.uniform(cmin, cmax), cmin, cmax)
                if data[indexes[j]]["source"] not in source_colors:
                    source_colors[data[indexes[j]]["source"]] = strRgb(random.uniform(cmin, cmax), cmin, cmax)

                G.add_node(data[indexes[i]]["source"] + " : " + data[indexes[i]]["title"], color=source_colors[data[indexes[i]]["source"]])
                G.add_node(data[indexes[j]]["source"] + " : " + data[indexes[j]]["title"], color=source_colors[data[indexes[j]]["source"]])
                G.add_edge(data[indexes[i]]["source"] + " : " + data[indexes[i]]["title"],
                           data[indexes[j]]["source"] + " : " + data[indexes[j]]["title"], color=strRgb(sim_matrix[i][j],cmin, cmax), weight=sim_matrix[i][j])

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
    vect = TfidfVectorizer(min_df=1, stop_words="english")
    tfidf = vect.fit_transform(corpus_normalized)
    pairwise_sim = tfidf * tfidf.T
    sim_matrix = pairwise_sim.A
    G = construct_graph(corpus, sim_matrix, data, corpus_normalized)
    print(G.number_of_nodes(), G.number_of_edges())
    nx.write_gexf(G, 'graph_en.gexf')