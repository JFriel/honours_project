from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://www.corenlp.run')

def stanfordOpenIE(sentence):
	data = nlp.annotate(sentence, properties={
	'annotators': 'tokenize, ssplit, pos, lemma,  depparse, natlog, openie',
	'outputFormat': 'json'
	})
        return data['sentences'][0]['openie'][0]
