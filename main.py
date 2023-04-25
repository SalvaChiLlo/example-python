from newspaper import Article
import nltk
from gtts import gTTS
import os

#Get the article
article = Article('https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt')
article.download()
article.parse()
nltk.download('punkt')
article.nlp()
#Get the articles text
mytext = article.text
language = 'en' #English
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("read_article.mp3")

