'use strict'
const HTML5Tokenizer = require("simple-html-tokenizer");

const data = "\
<REUTERS TOPICS=YES LEWISSPLIT=TRAIN CGISPLIT=TRAINING-SET OLDID=19419 NEWID=3001>\
<DATE> 9-MAR-1987 04:58:41.12</DATE>\
<TOPICS><D>money-fx</D></TOPICS>\
<PLACES><D>uk</D></PLACES>\
<PEOPLE></PEOPLE>\
<ORGS></ORGS>\
<EXCHANGES></EXCHANGES>\
<COMPANIES></COMPANIES>\
<UNKNOWN> \
&#5;&#5;&#5;RM\
&#22;&#22;&#1;f0416&#31;reute\
b f BC-U.K.-MONEY-MARKET-SHO   03-09 0095</UNKNOWN>\
<TEXT>&#2;\
<TITLE>U.K. MONEY MARKET SHORTAGE FORECAST AT 250 MLN STG</TITLE>\
<DATELINE>    LONDON, March 9 - </DATELINE><BODY>The Bank of England said it forecast a\
shortage of around 250 mln stg in the money market today.\
    Among the factors affecting liquidity, it said bills\
maturing in official hands and the treasury bill take-up would\
drain around 1.02 billion stg while below target bankers\
balances would take out a further 140 mln.\
    Against this, a fall in the note circulation would add 345\
mln stg and the net effect of exchequer transactions would be\
an inflow of some 545 mln stg, the Bank added.\
 REUTER\
&#3;</BODY></TEXT>\
</REUTERS>"

const generateText = (req,res) => {
    let article = {};
    let title = null;
    let date = null;
    let body = null;
    const tokens = HTML5Tokenizer.tokenize(data);
    for(var i =0; i < tokens.length; i++){
        if (tokens[i].tagName == "tITLE" && title === null){//broken on purpose
            title = tokens[i+1].chars;
        }
        if(tokens[i].tagName == "bODY" && body === null){
            body = tokens[i+1].chars;
        }
        if(tokens[i].tagName == "dATE" && date === null){
            date = tokens[i+1].chars;
        }
    }
    article.title = title;
    article.date = date;
    article.body = body;
    res.send([article]);
}

module.exports = {
  generateText:generateText
}
