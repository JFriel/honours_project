import dateutil.parser as dparse
import collections


def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]



def hasDate(sentence):
    try:
        date =  dparse.parse(sentence, fuzzy=True)
        if date.year <2016 and len(date.year) == 4:
            return date
        else:
            return []
    except:
        words= sentence.split()
        dates= []
        for word in words:
            try:
                date =  dparse.parse(word, fuzzy=True)
                if date.year != 2016:
                    dates.append(date)
            except:
                pass
        return flatten(dates)

