from HTMLParser import HTMLParser


with open('data.sgm', 'r') as myfile:
    data=myfile.read().replace('\n', '')

Y = ['<', '!', 'DOCTYPE', 'lewis', 'SYSTEM', 'lewis.dtd', '>', '<', 'REUTERS', 'TOPICS=YES', 'LEWISSPLIT=TRAIN', 'CGISPLIT=TRAINING-SET', 'OLDID=18419', 'NEWID=2001', '>', '<', 'DATE', '>', '5-MAR-1987', '09:07:54.17', '<', '/DATE', '>', '<', 'TOPICS', '>', '<', 'D', '>', 'earn', '<', '/D', '>', '<', '/TOPICS', '>', '<', 'PLACES', '>', '<', 'D', '>', 'uk', '<', '/D', '>', '<', '/PLACES', '>', '<', 'PEOPLE', '>', '<', '/PEOPLE', '>', '<', 'ORGS', '>', '<', '/ORGS', '>', '<', 'EXCHANGES', '>', '<', '/EXCHANGES', '>', '<', 'COMPANIES', '>', '<', '/COMPANIES', '>', '<', 'UNKNOWN', '>', '&', '#', '5', ';', '&', '#', '5', ';', '&', '#', '5', ';', 'F', '&', '#', '22', ';', '&', '#', '22', ';', '&', '#', '1', ';', 'f0986', '&', '#', '31', ';', 'reuted', 'f', 'BC-JAGUAR-SEES-STRONG-GR', '03-05', '0115', '<', '/UNKNOWN', '>', '<', 'TEXT', '>', '&', '#', '2', ';', '<', 'TITLE', '>', 'JAGUAR', 'SEES', 'STRONG', 'GROWTH', 'IN', 'NEW', 'MODEL', 'SALES', '<', '/TITLE', '>', '<', 'DATELINE', '>', 'LONDON', ',', 'March', '5', '-', '<', '/DATELINE', '>', '<', 'BODY', '>', 'Jaguar', 'Plc', '&', 'lt', ';', 'JAGR.L', '>', 'is', 'about', 'to', 'sell', 'itsnew', 'XJ-6', 'model', 'on', 'the', 'U.S.', 'And', 'Japanese', 'markets', 'and', 'expects', 'astrong', 'reception', 'based', 'on', 'its', 'success', 'in', 'the', 'U.K.', ',', 'Chairman', 'SirJohn', 'Egan', 'told', 'a', 'news', 'conference', '.']
Ystr = ''.join(Y)

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    start_tags =[]
    end_tags=[]
    tag_data = []

    def handle_starttag(self, tag, attrs):
        #print "Encountered a start tag:", tag
        self.start_tags.append(tag)

    def handle_endtag(self, tag):
        #print "Encountered an end tag :", tag
        self.end_tags.append(tag)

    def handle_data(self, data):
        #print "Encountered some data  :", data
        if len(self.start_tags) != len(self.end_tags):
            self.tag_data.append((self.start_tags[-1],data))


# instantiate the parser and fed it some HTML
def parse_data():
    parser = MyHTMLParser()
    parser.feed(data)
    return parser.tag_data


print parse_data()







