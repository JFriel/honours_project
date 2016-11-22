from textblob.classifiers import NaiveBayesClassifier


with open('data/train.csv', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="csv")


print cl.classify("International Book Year")