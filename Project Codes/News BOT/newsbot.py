import newsfeed
import time

news_articles = newsfeed.get_news("politics")
length = len(news_articles)
    
for i in range(0, length):
        print (news_articles[i]["title"])
        print ("\n")
        print (news_articles[i]["description"])
        print ("\n")
        print ("Source: " + news_articles[i]["source"]["name"] )
        print ("Link: " + news_articles[i]["url"])
        print ("\n")
        
        time.sleep(5)

