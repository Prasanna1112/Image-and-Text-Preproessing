#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
import glob
from skimage.io import imread


# In[3]:


# eg_file = glob.glob(r"/Downloads/")
im = imread(r'Downloads/Sample.jpeg')
plt.imshow(im)
plt.show()


# In[4]:


from PIL import Image
im = Image.open(r'Downloads/Sample.jpeg','r')
pix_val = list(im.getdata())
print(pix_val)


# In[5]:


pix_val_flat = [x for sets in pix_val for x in sets]
print(pix_val_flat)


# In[1]:


# Text Pre-Processing

import nltk
nltk.download()


# In[5]:


from nltk.tokenize import sent_tokenize, word_tokenize

text = "I am a beginner at programming, my friend, on the other hand is an expert in this. I would like to be like him."

print(sent_tokenize(text))


# In[6]:


print(word_tokenize(text))


# In[9]:


import re

text1 = "ThEsE is a SamplE for LoWERcaSe text."
text1 = re.sub(r"[^a-zA-Z0-9]", " ", text1.lower())
words = text1.split()
print(words)


# In[10]:


from nltk.corpus import stopwords

print(stopwords.words("english"))


# In[12]:


text2 = "I have 6 questions, 3 are solved, 1 remaining as 2 are being solved."

out = re.sub(r'\d+', '', text2)
print(out)


# In[14]:


# Importing inflect library to convert numbers to text

import inflect

p = inflect.engine()
  
# convert number to words
def numtotext(text):
    
    # split string into list of words
    temp_str = text.split()
    
    # empty list
    new_string = []
  
    for word in temp_str:
        
        # if word is a digit, convert the digit and append them to empty list
        
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)
  
        # if not a number, append the word as it is
        else:
            new_string.append(word)
  
    # join the words of new_string to form a string
    temp_str = ' '.join(new_string)
    return temp_str
  
org_str = 'I have 6 questions, 3 are solved, 1 remaining as 2 are being solved.'

numtotext(org_str)


# In[18]:


# Removing punctuations
import string

inp = "Do you know what the time is? I do not have a watch handy, I forgot it at home."
trans = str.maketrans('', '', string.punctuation)
print(inp.translate(trans))


# In[19]:


# Removing whitespaces

text3 = "        A lot of spaces in front of the senteces."
print(" ".join(text3.split()))


# In[20]:


#Stemming
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

text4 = 'Programming posseses a lot of methods, works on features, extraction of data and helps in digital world.'
word_tokens = word_tokenize(text4)
stems = [stemmer.stem(word) for word in word_tokens]
print(stems)


# In[22]:


# Lemmatization

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

text5 = 'Programming posseses a lot of methods, works on features, extraction of data and helps in digital world.'
word_tokens = word_tokenize(text5)

# provide part-of-speech
lemmat = [lemmatizer.lemmatize(word, pos ='v') for word in word_tokens]
print(lemmat)


# In[23]:


# Removing default stopwords

from nltk.corpus import stopwords
print(stopwords.words("english"))

text6 = "Sentence to remove stopwords from it. This is just a sample to see what stop words are there and we're going to see what words are removed."

stop_words = set(stopwords.words("english"))
word_tokens = word_tokenize(text6)
filtered = [word for word in word_tokens if word not in stop_words]

print(filtered)


# In[39]:


# Removing HTML characters

import html
from html.parser import HTMLParser

url_txt = " When downloaded nltk API, showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml showed up in output."
# url_txt = HTMLParser().unescape(url_txt)
url_txt = html.unescape(url_txt)
print("Before: {}".format(url_txt))

# API for regular expressions
import re

# Removing hyperlinks
url_txt = re.sub(r'https?:\/\/.\S+', "", url_txt)

# # remove old style retweet text "RT"
# tweet = re.sub(r'^RT[\s]+', '', tweet)

print("After: {}".format(url_txt))


# In[ ]:




