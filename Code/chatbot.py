# This codes are referenced from the Github repo (https://github.com/parulnith/Building-a-Simple-Chatbot-in-Python-using-NLTK/blob/master/chatbot.py)

# Loading the required packages

import nltk
import random
import string
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

# Setup

warnings.filterwarnings('ignore') # Ignore warning messages

f = open('corpus_linguistics.txt', 'r') # opening the corpus
text = f.read() # reading the corpus

# Convert all text from corpus to lower case

text = text.lower()

# Perform tokenization

sent_tokens = nltk.sent_tokenize(text)
word_tokens = nltk.word_tokenize(text)

# Initialize set of greetings and responses

user_greetings = ["hi", "hello", "good morning", "hey", "what's up"]
bot_greetings = ["Hello, how may I be of assistance?"]
user_gratitude = ["thank you", "thanks", "that was helpful"]
bot_gratitude = ["You're welcome! Is there anything else you need?",
                 "Happy to help! Are there other questions that I could help "
                 "with?"]
bot_exit_text = ["Thank you for using my services. Have a great day!",
                 "Hope I was helpful. See you later :)", "Bye!"]
languages = {"en": "English", "fr": "French", "es": "Spanish",
             "la": "Latin"}

# Text Preprocessing

lemmatizer = nltk.stem.WordNetLemmatizer() # Text Lemmatization

# Function to perform lemmatization

def LemTokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

# Function to perform normalization

def LemNormalize(text):
    return LemTokens(
        nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Generating response

def respond(input_text):
    bot_message = ""
    sent_tokens.append(input_text)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english') # TF-IDF approach
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        bot_message += "Apologies, I cannot understand your question. Please " \
                       "rephrase your question and try again. "
    else:
        bot_message += sent_tokens[idx]
    return bot_message

# Perform sentiment analysis

def extract_sentiment(text):
    processed_text = TextBlob(text) # Here, we use the textblob module to implement sentiment analysis
    sentiment = processed_text.sentiment
    if sentiment.polarity < 0: # we manually set the rule for testing the mood of a sentence
        return "negative"
    elif sentiment.polarity > 0:
        return "positive"
    else:
        return "neutral"

# Language detection

def get_language(text):
    processed_text = TextBlob(text)
    return processed_text.detect_language()

# Interact with chatbot framework based on input from user

def bot(choice, input_text):
    exit_status = False
    while exit_status is False:
        input_text = input_text.lower() # lowercase the input
        if input_text != 'bye':
            if choice == "1":
                if input_text in user_greetings: # Generate random response from the greetings set
                    return random.choice(bot_greetings)
                else:
                    if input_text in user_gratitude: # Generate random response from the gratitude set
                        return random.choice(bot_gratitude)
                    else:
                        return respond(input_text) # Generate a response using NLTK that answers the user's question
                        sent_tokens.remove(input_text)
            elif choice == "2":
                return_string = "Detected Language: " + languages[
                    get_language(input_text)] + "\n" # Language detection
                if get_language(input_text) == "en":
                    return_string += "Detected Sentiment: " + extract_sentiment(
                        input_text) # Sentiment analysis
                else:
                    return_string += "Sentiment can only be detected for " \
                                     "text in English "
                return return_string
            else:
                exit_status = True
                return "Invalid choice!\nOnly 1 and 2 are valid choices " \
                       "\nPlease try running the program again. "
        else:
            exit_status = True
            return random.choice(bot_exit_text)
