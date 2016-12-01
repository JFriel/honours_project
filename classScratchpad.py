import numpy as np
import sklearn.decomposition

def test(s1,s2):
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
                    D2[-1] += 1

    #print D1
    #print D2
    #print len(D1)
    #print len(D2)

    X = np.array([D1,D2])
    pca = sklearn.decomposition.TruncatedSVD(n_components=1)
    X = pca.fit_transform(X)
    A = (X[0][0])
    B =  X[1][0]
    return [A,B]

#two = ["Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn't so bad after all.","Yeah, I think it's a good environment for learning English.","I want to buy a onesie but know it won't suit me.","Joe made the sugar cookies; Susan decorated them."," He turned in the research paper on Friday; otherwise, he would have not passed the class. ","Is it free?"]

#one = ["I really want to go to work, but I am too sick to drive.","A song can make or ruin a person's day if they let it get to them.","My Mum tries to be cool by saying that she likes all the same things that I do.","Everyone was busy, so I went to the movie alone.","She only paints with bold colors; she does not like pastels."]

#test(one,two)
