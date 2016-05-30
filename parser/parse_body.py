




def parse_body(body):
    """By passing in the body of the text, we get all sentences with any important information
    such as dayes, timescales
    #TODO :- Locate subject name(s)
            Work out what other relative info there is
    ***ASSUME THE DATA IS ALREADY TOKENIZED***
    """
    important_sentences = get_times(body)
    for i in important_sentences:#this is all sentences that /may/ contain important info
        print i
        print "\n\n\n"



def get_times(sentences):
    weekday=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    months = ['january','february','march','april','may','june','july','august','september','october','november','december']
    timescale = ['week','month','year','day','days']


    important_sentences=[]

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
    return important_sentences


def is_year(string):
    try:
        int(string)
        if len(string) ==4:
            return True
    except:
        return False


