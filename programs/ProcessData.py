import nltk
import unicodedata
import re

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/words')
except LookupError:
     nltk.download('words')

#try:
#    nltk.data.find('sentiment/vader_lexicon')
#except LookupError:
#    nltk.download('vader_lexicon')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

#try:
#    nltk.data.find('tokenizers/punkt')
#except LookupError:
#    nltk.download('wordnet')

#class ProcessData:
#    
#    def __init__(self,x):
#        
#        self.GetSentenceTokens(x)
#        self.Normalize(x)
        
def GetSentenceTokens(x):
    y=nltk.sent_tokenize(x)
    return y    
        
def _remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in nltk.corpus.stopwords.words('english'):
            new_words.append(word)
    return new_words
    
def _lower(x):
    norm=[word.lower() for word in x]
    return norm

def _remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def _remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def Normalize(x):
    x1=nltk.word_tokenize(x)
    x2=_remove_stopwords(x1)
    x3=_remove_punctuation(x2)
    x4=_remove_non_ascii(x3)
    x5=_lower(x4)
    return x5
    