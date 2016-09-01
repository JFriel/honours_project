from BeautifulSoup import BeautifulSoup;

def parse(document):
    soupData = BeautifulSoup(document);
    for article in soupData('reuters'):
        print("yay");
