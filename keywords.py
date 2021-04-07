#coding: utf-8
import json
import math
from operator import itemgetter

from deep_translator import GoogleTranslator

def read_json_file():
    file = open("data.json", 'r' , encoding="utf8")
    data = json.load(file)
    return data

def convert_data_to_text(data, catch=None):
    lenght = len(data)
    wrong_language="ro"
    data_to_text = ""
    array_of_texts = []
    for i in range(lenght):
        if data[i]['language'] != wrong_language:
            for text in data[i]['body']:
                data_to_text += text
        """
         else:
            for text in data[i]['body']:
                try:
                  data_to_text += translate_text(text)
                except:
                  print("Text lenght over 5000 characters...")
        """


    return data_to_text

def translate_text(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated

def get_stop_words():
    stop_words = "‘ourselves’, ‘hers’, ‘between’, ‘yourself’, ‘but’, ‘again’, ‘there’, ‘about’, ‘once’, ‘during’, ‘out’, ‘very’, ‘having’, ‘with’, ‘they’, ‘own’, ‘an’, ‘be’, ‘some’, ‘for’, ‘do’, ‘its’, ‘yours’, ‘such’, ‘into’, ‘of’, ‘most’, ‘itself’, ‘other’, ‘off’, ‘is’, ‘s’, ‘am’, ‘or’, ‘who’, ‘as’, ‘from’, ‘him’, ‘each’, ‘the’, ‘themselves’, ‘until’, ‘below’, ‘are’, ‘we’, ‘these’, ‘your’, ‘his’, ‘through’, ‘don’, ‘nor’, ‘me’, ‘were’, ‘her’, ‘more’, ‘himself’, ‘this’, ‘down’, ‘should’, ‘our’, ‘their’, ‘while’, ‘above’, ‘both’, ‘up’, ‘to’, ‘ours’, ‘had’, ‘she’, ‘all’, ‘no’, ‘when’, ‘at’, ‘any’, ‘before’, ‘them’, ‘same’, ‘and’, ‘been’, ‘have’, ‘in’, ‘will’, ‘on’, ‘does’, ‘yourselves’, ‘then’, ‘that’, ‘because’, ‘what’, ‘over’, ‘why’, ‘so’, ‘can’, ‘did’, ‘not’, ‘now’, ‘under’, ‘he’, ‘you’, ‘herself’, ‘has’, ‘just’, ‘where’, ‘too’, ‘only’, ‘myself’, ‘which’, ‘those’, ‘i’, ‘after’, ‘few’, ‘whom’, ‘t’, ‘being’, ‘if’, ‘theirs’, ‘my’, ‘against’, ‘a’, ‘by’, ‘doing’, ‘it’, ‘how’, ‘further’, ‘was’, ‘here’, ‘than’".replace('‘','').replace('‘','').replace(',','')
    stop_words = stop_words.replace('’', '')
    stop_words = stop_words.replace('‘', '')
    stop_words = stop_words.replace(',', '')
    stop_words = stop_words.split(" ")
    stop_words.append('A')

    return stop_words

def calculate_TF_and_IDF(text):
    stop_words = get_stop_words()

    total_sentences = text.split(".")
    try:
         total_sentences.remove('')
    except:
        print("No need to split last dot ...")

    total_sent_len = len(total_sentences)

    total_words = text.split()
    total_word_length = len(total_words)

    tf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.', '')
        if each_word not in stop_words:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1

    # Dividing by total_word_length for each dictionary element
    tf_score.update((x, y / int(total_word_length)) for x, y in tf_score.items())
   # print(tf_score)

    idf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.', '')
        if each_word not in stop_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1

    # Performing a log and divide
    try:
        idf_score.update((x, math.log(int(total_sent_len) / y)) for x, y in idf_score.items())
    except:
        print("Division by zero exception")

   # print(idf_score)
    return(tf_score, idf_score)



def calculate_IDF_multiplied_TF(tf_score, idf_score):
    tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
    return tf_idf_score

def check_sent(word, sentences):
    final = [all([w in x for w in word]) for x in sentences]
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n])
    return result

if __name__ == "__main__":
    nomber_of_words = 1000
    data = read_json_file()
    text = convert_data_to_text(data)
    #text = "A jury pool has been appointed in the case of the ex-Minneapolis police officer accused of killing George Floyd, an unarmed black man, last year. Mr Chauvin, 44, is accused of unintentional murder and manslaughter in the 25 May, 2020 death of Mr Floyd. Arguments will begin on 29 March, with 14 of the jurors seated. Jurors for the case, for which race has been at the centre, include three black men, one black woman, two white men, five white women and two multiracial women, according to the court. Their identities will remain anonymous for their safety. Hennepin County Judge Peter Cahill said on Tuesday that he would not release the rest of the jury pool until the 14 selected jurors are officially sworn in on 29 March. Mr Chauvin was the Minneapolis officer filmed kneeling on Mr Floyd's neck for over seven minutes in a video that sparked protests over racial inequalities worldwide. He faces a maximum penalty of 40 years in prison for the second-degree murder and manslaughter charges. A third-degree murder charge, with a maximum penalty of 25 years, was also reinstated earlier this month. Of the dozens of people I interviewed in Minneapolis, they all the same opinion on one issue: seating a jury would be hard. Beyond that, opinions varied; some believed the trial would be fair; others saw it as a sham. Regarding the issue of jury selection, they had good reasons for concern: the makeup of the jury lies at the heart of the matter, and will determine whether the trial is fair."
    part_of_text_1 = text[ :100000]
    print("Text is saved ...")
    tf_score, idf_score = calculate_TF_and_IDF(text)
    print("Tf score and Idf score is calculated ...")
    tf_idf_score = calculate_IDF_multiplied_TF(tf_score,idf_score)
    print("TF and IDF is multiplicated")
    top_n_keywords = get_top_n(tf_score, nomber_of_words)
    print ("TOP ", nomber_of_words , "keywords ...")
    print(top_n_keywords)
    #print(total_sentences)


