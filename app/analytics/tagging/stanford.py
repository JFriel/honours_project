from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost:9000')

def stanfordOpenIE(sentence):
	data = nlp.annotate(sentence, properties={
	'annotators': 'tokenize, ssplit, pos, lemma,  depparse, natlog, openie',
	'outputFormat': 'json'
	})
        returndata = {}
        return data['sentences'][0]['openie']

