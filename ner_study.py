import webScraping as ws
import aux_functions as af
import os
import spacy

# news websites URLs
URL_list = [
    "https://www.washingtonpost.com/",
    "https://www.nytimes.com/",
    "https://www.theguardian.com/international",
    "https://edition.cnn.com/",
    "https://www.reuters.com/",
    "https://www.wsj.com/",
    "https://www.huffpost.com/",
    "https://abcnews.go.com/",
    "https://www.thesun.co.uk/",
    "https://www.dailymail.co.uk/home/index.html"
]

folder = "news_html"

if not os.path.exists(folder):
    os.mkdir(folder)

path = os.getcwd() + "/" + folder

ws.create_mini_dataset(path, URL_list)

news_texts = af.create_text_dict(path)

nlp = spacy.load('en_core_web_sm')

for i in range(0, len(news_texts)):
    temp_doc = nlp(news_texts[i]["text"])
    temp_list = []
    for ent in temp_doc.ents:
        temp_list.append((ent.text, ent.label_))
    news_texts[i]["entities"] = temp_list


# detect only person entities

