from textblob.classifiers import MaxEntClassifier



with open('data/train-toy.csv', 'r') as fp:
    cl = MaxEntClassifier(fp, format="csv")


with open('data/test-toy.csv', 'r') as gp:
    print cl.accuracy(gp, format="csv")

