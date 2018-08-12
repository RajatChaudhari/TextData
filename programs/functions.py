import nltk
import unicodedata
import re
nltk.download('punkt')
nltk.download('words')
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('wordnet')

class ProcessData:
    
    def __init__(self,x):
        
        self.GetSentenceTokens(x)
        self.Normalize(x)
        
    def GetSentenceTokens(self,x):
        y=nltk.sent_tokenize(x)
        return y    
        
    def remove_stopwords(self,words):
        """Remove stop words from list of tokenized words"""
        new_words = []
        for word in words:
            if word not in nltk.corpus.stopwords.words('english'):
                new_words.append(word)
        return new_words
    
    def lower(self,x):
        norm=[word.lower() for word in x]
        return norm

    def remove_non_ascii(self,words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words

    def remove_punctuation(self,words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words

    def Normalize(self,x):
        x1=nltk.word_tokenize(x)
        x2=self.remove_stopwords(x1)
        x3=self.remove_punctuation(x2)
        x4=self.remove_non_ascii(x3)
        x5=self.lower(x4)
        return x5
    