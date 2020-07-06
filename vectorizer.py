
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

# Tokenization
def tokenize(text):
    tokens = word_tokenize(text)
    return tokens

def tokenizeSentence(para):
    sentences = sent_tokenize(para)
    tokens = []
    for sentence in sentences:
        tokens.extend(tokenize(sentence))
    return tokens

# Lemmatization
def lemmat(tokens):
    lemmatizer = WordNetLemmatizer()
    tokens=[lemmatizer.lemmatize(word) for word in tokens]
    return tokens

# Stemming
def stem(tokens):
    tokens=word_tokenize(text.lower())
    ps = PorterStemmer()
    tokens=[ps.stem(word) for word in tokens]
    return tokens

# Stop words
def stopWords(tokens):
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [j for j in tokens if j not in stopwords]
    return tokens

def normalize(tokens):
    puncts=['.','?','!','""',"''",","]
    tokens = [j.lower() for j in tokens if j not in puncts]
    return tokens

def vectorize(text):
    tokens = tokenizeSentence(text)
    tokens = stem(tokens)
    tokens = stopWords(tokens)
    tokens = normalize(tokens)
    print(tokens)


text = "Hello, My Name is Arman. I am very happy cos I started learning the sentimental analysis"
sentence = "This is a sample sentence.\n I am very happy today that I started learning nlp.\n I am findind it intriguing as till now.\n"
#vectorizeSentence(sentence)
vectorize(sentence)
