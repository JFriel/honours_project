from getTokens import tokens

from parse_body import parse_body

Y= "<!DOCTYPE lewis SYSTEM lewis.dtd><REUTERS TOPICS=YES LEWISSPLIT=TRAIN CGISPLIT=TRAINING-SET OLDID=18419 NEWID=2001><DATE> 5-MAR-1987 09:07:54.17</DATE><TOPICS><D>earn</D></TOPICS><PLACES><D>uk</D></PLACES><PEOPLE></PEOPLE><ORGS></ORGS><EXCHANGES></EXCHANGES><COMPANIES></COMPANIES><UNKNOWN> &#5;&#5;&#5;F&#22;&#22;&#1;f0986&#31;reuted f BC-JAGUAR-SEES-STRONG-GR   03-05 0115</UNKNOWN><TEXT>&#2;<TITLE>JAGUAR SEES STRONG GROWTH IN NEW MODEL SALES</TITLE><DATELINE>    LONDON, March 5 - </DATELINE><BODY>Jaguar Plc &lt;JAGR.L> is about to sell itsnew XJ-6 model on the U.S. And Japanese markets and expects astrong reception based on its success in the U.K., Chairman SirJohn Egan told a news conference.    Commenting on an 11 pct growth in 1986 group turnover to830.4 mln stg and pre-tax profits at 120.8 mln stg, slightlybelow 1985's 121.3 mln, Egan said Jaguar aimed at an averageprofit growth of 15 pct per year. However, the introduction ofthe new model had kept this year's pre-tax profit down.    Jaguar starts selling XJ-6 in the U.S. In May and plans tosell 25,000 of its total 47,000 production there in 1987.    U.S. Sales now account for 65 pct of total turnover,finance director John Edwards said.    A U.S. Price for the car has not been set yet, but Edwardssaid the relatively high car prices in dollars of West Germancompetitors offered an umbrella for Jaguar. He added the XJ-6had also to compete with U.S. Luxury car producers which wouldrestrict the car's price.    Jaguar hedges a majority of its dollar receipts on a12-month rolling basis and plans to do so for a larger part ofits receipts for longer periods, John Egan said.    In the longer term, capital expenditure will amount to 10pct of net sales. Research and development will cost four pctof net sales and training two pct.    Jaguar builds half of its cars and buys components for theother half. The firm is in early stages of considering thebuilding of an own press shop in Britain for about 80 mln stg,but Egan said this would take at least another three years    On the London Stock Exchange, Jaguar's shares were lastquoted at 591p, down from 611p at yesterday's close, afterreporting 1986 results which were in line with marketexpectations, dealers said. REUTER...&#3;</BODY></TEXT></REUTERS>"

def tag_remover(article):
    """works well, the first sentence is all the article data when dealing with reuters"""
    tokenized_article = tokens(article)
    for sentence in tokenized_article:
        if ('<' or '>') in sentence:
            #TODO
            #run the metadata parser
        else:
            parse_body(sentence)

tag_remover(Y)
