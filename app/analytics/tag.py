import tagging.entityFinder as ef
import tagging.stanford as sf
import sys

def getTags(data, tagger):
        stanford = sf.stanfordOpenIE(data)
        if(len(stanford) == 0):
            #sys.exit("Couldn't run OpenIE on this.")
            return []#ef.entityFinder(data)
        return stanford[-1]
