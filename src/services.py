import requests
import json
from collections import Counter
from config import LIMIT, API_KEY, FILE
import re


def get_story_keywords(title, content):
    keywords =  [w.lower() for w in title.split() if len(w)>2]
    contntWords = dict(Counter(re.split(r"\W", content.lower())))
    for word in contntWords:
        if contntWords[word] > 2 and len(word) > 3:
            keywords.append(word)
    return keywords


def prepare_keywords_string(keywords, limit):
    for i in range(len(keywords)):
        new_join = '+'.join(keywords[:i+1])
        if len(new_join) > limit:
            return '+'.join(keywords[:i])
    return '+'.join(keywords)


def get_cover(story):
    keywords = get_story_keywords(story['title'], story['content'])
    q_string = prepare_keywords_string(keywords, LIMIT)
    url = 'https://pixabay.com/api/?key={}&q={}'.format(API_KEY, q_string)
    response = requests.get(url).json()
    if response['totalHits'] == 0:
        url = 'https://pixabay.com/api/?key={}&q={}'.format(API_KEY, keywords[0])
        response = requests.get(url).json()
    return response['hits'][0]['webformatURL']


def save_to_file(record):
    with open(FILE, 'w') as file:
        json.dump(record, file)
    return load_file()


def load_file():
    with open(FILE) as json_file:
        stories = json.load(json_file)
    return stories