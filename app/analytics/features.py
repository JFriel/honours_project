import numpy as np
import sklearn.decomposition

def get(s1,s2):
    words = []
    for s in s1:
        #for w in s:
        w = s.split()
        words.extend(w)
    for s in s2:
        #for w in s:
        w = s.split()
        words.extend(w)

    words = set(words)

    D1 = []
    D2 = []
    for word in words:
        D1.append(0)
        D2.append(0)
        for s in s1:
            wr = s.split()
            for w in wr:
                if w == word:
                    D1[-1] += 1
        for s in s2:
            wr = s.split()
            for w in wr:
                if w == word:
                    D2[-1] += 1
                    
    #print D1
    #print D2
    #print len(D1)
    #print len(D2)
    #print D1
    #print D2
    #print len(D1)
    #print len(D2)
    return D1[0:60]
    
    #X = np.array([D1,D2])
    #pca = sklearn.decomposition.TruncatedSVD(n_components=1)
    #X = pca.fit_transform(X)
    #A = float(X[0][0])
    #B = float(X[1][0])
    #return [A,B]

def get2(s1,s2):
    words = []
    for s in s1:
        for w in s:
            words.append(w)
    for s in s2:
        for w in s:
            words.append(w)

    words = set(words)

    D1 = []
    D2 = []
    for word in words:
        D1.append(0)
        D2.append(0)
        for s in s1:
            for w in s:
                if w == word:
                    D1[-1] += 1
        for s in s2:
            for w in s:
                if w == word:
                    D1[-1] += 1

    #print D1
    #print D2
    #print len(D1)
    #print len(D2)
    #X = np.array([D1])
    #pca = sklearn.decomposition.TruncatedSVD(n_components=1)
    #X = pca.fit_transform(X)
    #A = (X[0][0])
    #B =  X[1][0]
    return D1[0:15]

def get3(s1,s2,s3):
    words = []
    for s in s1:
        for w in s:
            words.append(w)
    for s in s2:
        for w in s:
            words.append(w)
    for s in s3:
        for w in s:
            words.append(w)

    words = set(words)

    D1 = []
    D2 = []
    D3 = []
    for word in words:
        D1.append(0)
        D2.append(0)
        D3.append(0)
        for s in s1:
            for w in s:
                if w == word:
                    D1[-1] += 1
        for s in s2:
            for w in s:
                if w == word:
                    D2[-1] += 1
        for s in s3:
            for w in s:
                if w == word:
                    D3[-1] += 1

    #print D1
    #print D2
    #print len(D1)
    #print len(D2)

    X = np.array([D1,D2,D3])
    #X = X.reshape
    pca = sklearn.decomposition.TruncatedSVD(n_components=1)
    X = pca.fit_transform(X)
    A = float(X[0][0])
    B = float(X[1][0])
    C = float(X[2][0])
    return [A,B,C]

    
   
two = ["Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn't so bad after all.","Yeah, I think it's a good environment for learning English.","I want to buy a onesie but know it won't suit me.","Joe made the sugar cookies; Susan decorated them."," He turned in the research paper on Friday; otherwise, he would have not passed the class. ","Is it free?"]

one = ["I really want to go to work, but I am too sick to drive.","A song can make or ruin a person's day if they let it get to them.","My Mum tries to be cool by saying that she likes all the same things that I do.","Everyone was busy, so I went to the movie alone.","She only paints with bold colors; she does not like pastels."]

#print type(get2(one,two))
#print type(get(one,two))
print get3(one,two,one)
