import os
from nltk import tokenize,word_tokenize


os.chdir('../bbc/business')#can change this to the correct dataset


def parse():
    for data_file in os.listdir(os.getcwd()):
        tokenized_sentences  = []
        data_point = open(data_file)
        raw_text = data_point.read()
        sentences = tokenize.sent_tokenize(raw_text)
        for sentence in sentences:
            tokenized_sentence = word_tokenize(sentence)
            tokenized_sentences.append(tokenized_sentence)
        decision_tree(tokenized_sentences)
        print tokenized_sentences
        break#remove this to do all data seets, but lets just test for one atm




parse()

