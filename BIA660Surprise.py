#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:49:45 2020

@author: ruizhihao
"""

import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = '/Users/ruizhihao/stanford-corenlp-full-2018-10-05/stanford-parser-full-2018-10-17'
os.environ['STANFORD_MODELS'] = '/Users/ruizhihao/stanford-corenlp-full-2018-10-05/stanford-parser-full-2018-10-17'

parser = stanford.StanfordParser(model_path="/Users/ruizhihao/stanford-corenlp-full-2018-10-05")
sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your name?"))
print(sentences)

# GUI
for line in sentences:
    for sentence in line:
        sentence.draw()
        
        
import nltk
sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
tokens
tagged = nltk.pos_tag(tokens)

entities = nltk.chunk.ne_chunk(tagged)
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]


from nltk.parse.stanford import StanfordParser
eng_parser = StanfordParser(r"/Users/ruizhihao/stanford-corenlp-full-2018-10-05/stanford-parser-full-2018-10-17/stanford-parser.jar",r"/Users/ruizhihao/stanford-corenlp-full-2018-10-05/stanford-parser-full-2018-10-17/stanford-parser-3.9.2-models.jar",r"/Users/ruizhihao/stanford-corenlp-full-2018-10-05/stanford-parser-full-2018-10-17/englishPCFG.ser.gz")

print(list(eng_parser.parse("the quick brown fox jumps over the lazy dog".split())))


from nltk.tree import Tree
parsetree = Tree.fromstring(list(eng_parser.parse("the quick brown fox jumps over the lazy dog".split())))

import nltk
sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
tokens = nltk.word_tokenize(sentence)
tokens

str(tokens)
sentence =eng_parser.raw_parse(str(tokens))
print(sentence)
for line in sentence:
    print(line)
    
    



