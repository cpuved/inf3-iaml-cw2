#!/usr/bin/env python
# coding: utf-8

# In[1]:


def readLangs():
    file = open("../data/languages.txt", "r")  
    lang_names = []
    lang_codes= []
    for i in range(22):
        read = file.readline().split()
        lang_names.append(read[1])
        lang_codes.append(read[2][1:-1])   
    file.close()
    
    return lang_names, lang_codes

