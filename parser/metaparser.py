

def meta_parser(sentence):
    meta_data=[]#list of tuples of the form (name,[x,y,x])
    for i in range(len(sentence)):
        if sentence[i] == '<':
            header=[]
            body = []
            i++
            while sentence[i] != '>':#gets the tag name
                header.append(sentence[i])
            i++
            while sentence[i] != '<' and sentence[i+1] != '/':#check if we're ending the tag
                body.append(sentence[i]
            i = i+4#this should take us tast the exit tag
