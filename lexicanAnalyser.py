# -*- coding: utf-8 -*-

################################Vader Demo#####################################

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
print(analyser.polarity_scores("This is a good course")['compound'])
analyser.polarity_scores("This is an awesome course") # degree modifier
analyser.polarity_scores("The instructor is so cool")
analyser.polarity_scores("The instructor is so cool!!") # exclaimataion changes score
analyser.polarity_scores("The instructor is so COOL!!") # Capitalization changes score
analyser.polarity_scores("Machine learning makes me :)") #emoticons
analyser.polarity_scores("His antics had me ROFL")
analyser.polarity_scores("The movie SUX") #Slangs


################################Textblob Demo##################################

from textblob import TextBlob

print(TextBlob("His").sentiment)
TextBlob("remarkable").sentiment
TextBlob("work").sentiment
TextBlob("ethic").sentiment
print(TextBlob("impressed").sentiment)
TextBlob("me").sentiment
print(TextBlob("His remarkable work ethic impressed me").sentiment)
