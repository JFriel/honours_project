from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost:9000')

def stanfordOpenIE(sentence):
	return nlp.annotate(sentence, properties={
	'annotators': 'tokenize, ssplit, pos, lemma,  depparse, natlog, openie',
	'outputFormat': 'json'
	})

