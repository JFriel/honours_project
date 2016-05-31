from metaparser import *
from getTokens import tokens

def parse(data):

    tag_body = parse_data(data)#returns a list of tuples (tage,data)
    for tag_set in tag_body:
        if tag_set[0] == 'body':
            #parse_body
        else:
            #Use the metadata to aid timeline

with open('data.sgm', 'r') as myfile:
    data=myfile.read().replace('\n', '')

parse(data)

