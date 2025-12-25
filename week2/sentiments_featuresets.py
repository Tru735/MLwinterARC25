import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
import random, pickle, os
from collections import Counter

lem = WordNetLemmatizer()
hm_lines = 100000

def create_lexicon(pos, neg):
    lexicon = []
    for fi in [pos, neg]:
        with open(fi, 'r') as f:
            content = f.readlines()
            for l in content[:hm_lines]:
                words = word_tokenize(l.lower())
                lexicon += list(words)
    lexicon = [lem.lemmatize(i) for i in lexicon]
    word_count = Counter(lexicon)
    l2 = []
    for w in word_count:
        if 50<word_count[w]<1000:
            l2.append(w)
    print(f"Lexicon size: {len(l2)}")
    return l2

def sample_handling(data, lexicon, classification):
    featureset =[]
    with open(data, 'r') as f:
        content = f.readlines()
        for l in content[:hm_lines]:
            words = word_tokenize(l.lower())
            words = [lem.lemmatize(i) for i in words]
            features = np.zeros(len(lexicon))
            for w in words:
                if w in lexicon:
                    features[lexicon.index(w)] +=1
            features = list(features)
            featureset.append([features, classification])
    return featureset

def create_dataset(pos, neg, test_size = 0.2):
    lexicon = create_lexicon(pos, neg)
    features = []
    features += sample_handling(pos, lexicon, [1,0])
    features += sample_handling(neg, lexicon, [0,1])
    random.shuffle(features)
    
    featuresx = np.array([f for (f,y) in features] , dtype=np.float32)
    featuresy = np.array([y for (f,y) in features] , dtype=np.float32)
    
    testing_size = int(test_size*len(features))
    
    train_x = list(featuresx[:,0][:-testing_size])
    train_y = list(featuresy[:,1][:-testing_size])
    
    test_x = list(featuresx[:,0][-testing_size:])
    test_y = list(featuresy[:,1][-testing_size:])
    
    return train_x, train_y, test_x, test_y

if __name__ == '__main__':
    pos = 'pos.txt'
    neg = 'neg.txt'
    train_x, train_y, test_x, test_y = create_dataset(pos, neg)
    with open('sentiment_set.pickle', 'wb') as f:
        pickle.dump((train_x, train_y, test_x, test_y), f)
    print("Dataset created and saved to sentiment_set.pickle")
        