import feedparser
from flask import Flask, render_template

app = Flask(__name__)


News_FEED = {'bbc' : 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn' : 'http://rss.cnn.com/rss/edition.rss',
             'fox' : 'http://feeds.foxnews.com/foxnews/latest',
             'iol' : 'http://www.iol.co.za/cmlink/1.640'}


@app.route("/")
@app.route("/<feeder>")
def get_news(feeder="bbc"):
    feed = feedparser.parse(News_FEED[feeder])
    return render_template("home.html",
            articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
