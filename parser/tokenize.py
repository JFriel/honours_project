from nltk import tokenize, word_tokenize

def get_tokens(document):
    tokenized_sentences  = []
    sentences = tokenize.sent_tokenize(document)
    for sentence in sentences:
        tokenized_sentence = word_tokenize(sentence)
        tokenized_sentences.append(tokenized_sentences)
    return tokenized_sentences


