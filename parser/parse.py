import os
from nltk import tokenize,word_tokenize


os.chdir('../bbc/business')#can change this to the correct dataset


important_sentences=[]

def parse():

    for data_file in os.listdir(os.getcwd()):
        tokenized_sentences  = []
        data_point = open(data_file)
        raw_text = data_point.read()
        sentences = tokenize.sent_tokenize(raw_text)
        for sentence in sentences:
            tokenized_sentence = word_tokenize(sentence)
            tokenized_sentences.append(tokenized_sentence)
        get_times(tokenized_sentences)
        for i in important_sentences:
            print i
            print "\n\n\n"

        print "\n\n"
        #print tokenized_sentences
        if(i==2):
            break#remove this to do all data seets, but lets just test for one atm


def get_times(sentences):
    weekday=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    months = ['january','february','march','april','may','june','july','august','september','october','november','december']
    timescale = ['week','month','year','day','days']


    for sentence in sentences:
        for i in range(0,len(sentence)):
            if sentence[i].lower() in weekday:#Day Of Week
                #print sentence[i]
                important_sentences.append(sentence)
            if sentence[i].lower() in months:
                #print sentence[i]
                important_sentences.append(sentence)
            if sentence[i].lower() in timescale:#Timescale
                #print sentence[i]
                important_sentences.append(sentence)
            if is_year(sentence[i]):
                #print sentence[i]
                important_sentences.append(sentence)


def is_year(string):
    try:
        int(string)
        if len(string) ==4:
            return True
    except:
        return False
parse()

