from app.parser.parser import parse;
import os;

data = open(os.path.join('./data/reuters/reut_002.sgm'));

print(parse(data));

