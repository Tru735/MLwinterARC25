import tensorflow as tf
from tensorflow import keras
import pickle

model = keras.models.load_model('sentiment_model.h5')

with open('lexicon.pickle', 'rb') as f:
    lexicon = pickle.load(f)

def convert_to_features(sentence, lexicon):
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer
    import numpy as np

    lem = WordNetLemmatizer()
    words = word_tokenize(sentence.lower())
    words = [lem.lemmatize(i) for i in words]
    features = np.zeros(len(lexicon))
    for w in words:
        if w in lexicon:
            features[lexicon.index(w)] += 1
    return np.array(features, dtype=np.float32).reshape(1, -1)

def predict_sentiment(sentence):
    features = convert_to_features(sentence, lexicon)
    prediction = model.predict(features)
    predicted_class = tf.argmax(prediction, axis=1).numpy()[0]
    if predicted_class == 0:
        return "Positive Sentiment :) "
    else:
        return "Negative Sentiment :( "
    
if __name__ == "__main__":
    test_sentence = " "
    while test_sentence.lower() != "exit":
        result = predict_sentiment(test_sentence)
        print(result)
        test_sentence = input("Enter a sentence to analyze sentiment (or type 'exit' to quit): ")