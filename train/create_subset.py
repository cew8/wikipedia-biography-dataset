import os
import json
from collections import defaultdict

indexes = (idx for idx in open('train.nb', 'r'))
sentences = (sent for sent in open('train.sent', 'r'))

articles = defaultdict(list)

for article_nr, idx in enumerate(indexes, 1):
    n_sentences = idx[:idx.find('\n')]
    for n in range(int(n_sentences)):
        articles[article_nr].append(next(sentences))
    if article_nr % 10 == 0:
        break

with open('biography_subset.json', 'wt') as f:
    json.dump(articles, f)
