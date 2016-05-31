from HTMLParser import HTMLParser

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
def parse_data(data):
    parser = MyHTMLParser()
    parser.feed(data)
    return parser.tag_data









