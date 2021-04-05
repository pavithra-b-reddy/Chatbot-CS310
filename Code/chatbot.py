import nltk
import ssl
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import pandas as pd


def setup():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    #f = open('corpus.txt','r')
    f = open('corpus_linguistics.txt','r')
    text = f.read()
    text = text.lower()
    sent_tokens = nltk.sent_tokenize(text)
    word_tokens = nltk.word_tokenize(text)

    user_greetings = ["hi", "hello", "good morning", "hey", "what's up"]
    bot_greetings = ["Hello, how may I be of assistance?"]
    user_gratitude = ["thank you", "thanks", "that was helpful"]
    bot_gratitude = ["You're welcome! Is there anything else you need?", "Happy to help! Are there other questions that I could help with?"]
    bot_exit_text = ["Thank you for using my services. Have a great day!", "Hope I was helpful. See you later :)", "Bye!"]
    languages = {"en":"English", "fr":"French", "es":"Spanish", "la":"Latin"}

def LemTokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
lemmatizer = nltk.stem.WordNetLemmatizer()

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



def respond(input_text):
    bot_message = ""
    sent_tokens.append(input_text)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        bot_message = "Apologies, I cannot understand your question. Please rephrase your question and try again."
    else:
        bot_message = sent_tokens[idx]
    return bot_message

def extract_sentiment(text):
    processed_text = TextBlob(text)
    sentiment = processed_text.sentiment
    if sentiment.polarity < 0:
        return "negative"
    elif sentiment.polarity > 0:
        return "positive"
    else:
        return "neutral"

def get_language(text):
    processed_text = TextBlob(text)
    return processed_text.detect_language()

if choice == 1:
    print("I can answer any questions you may have about machine intelligence. Type in your question. If want to exit, type bye.\n")

def bot(choice, input_text):
    exit_status = False
    while exit_status is False:
        input_text = input_text.lower()
        if input_text != 'bye':
            if choice == 1:
                if input_text in user_greetings:
                    return(random.choice(bot_greetings))
                else:
                    if input_text in user_gratitude:
                        return(random.choice(bot_gratitude))
                    else:
                        return(respond(input_text))
                        sent_tokens.remove(input_text)
            elif choice == 2:
                return_string = "Detected Language: " + languages[get_language(input_text)] + "\n"
                if get_language(input_text) == "en":
                    return_string += "Detected Sentiment: ", extract_sentiment(input_text)
                else:
                    return_string += "Sentiment can only be detected for text in English"
                return return_string
            else:
                exit_status = True
                return "Invalid choice!\nOnly 1 and 2 are valid choices \nPlese try running the program again."
        else:
            exit_status = True
            return random.choice(bot_exit_text)
