# sentiment-analysis

Steps for Sentimemtal Analysis Process -:

Vectoristion - The process of converting the raw data into form that machine can ingest

Steps for Vectorization are as follows -:
1. Tokenization : Process of breaking down the input stream into fundamental unit of processing. e.g. - Breaking sentences into words, phrases etc. which are called tokens.
2. Lemmatization : removing the inflection form of the words, that is keeping only cannonical form of a word. e.g - studying,studies,studied becomes study
3. Stemming : removing any non cannonical form of any words
4. Stop words: removing stop words which are sort of helping words or connectors to form the sentences in a language. e.g in english language - a,the,on etc.
5. Normalization : cleaning data, removing punctuation marks, emoticons etc.

The vectorized output of a document will be a vector of words


Lexican Based Approach to Sentimental Analysis:
This analysis is based on predetermined underlying sentiment behind lexicons(words).
Every lexicon has a quantative value associated with it, which determines its polarity.
For e.g. - for english language- excellent, wonderful can have value close to 1 associated with them.
and words likes terrible, pathetic can have value close to -1 associated with them.

Pros:
Inability to process acronyms,emoticons,slangs etc.
Not good for analysing sentiment intensity
Not able to process Sarcasm



VADER = Valence Aware Dictionary and Sentiment Reasonator
Python Library for Lexicon based Sentimental Analysis
