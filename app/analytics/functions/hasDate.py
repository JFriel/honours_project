from dateutil.parser import parse


def hasDate(sentence):
    try:
        return parse(sentence, fuzzy=True)
    except:
        return False
