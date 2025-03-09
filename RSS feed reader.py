import feedparser
url_to_parse="https://feedparser.readthedocs.io/en/latest/examples/rss20.xml"
def rss_feed_reader():
    try:
        url=input("Give me the url: ")
    except:
        print("This is not a valid url")
    try:
        res=feedparser.parse(url)
        print(f"Title: {res.feed.title}")
        print(f"Description: {res.feed.description}")
        print(f"Link: {res.feed.link}")
    except:
        print("This url doesn't have a title or description or link!!!")
    
rss_feed_reader()



