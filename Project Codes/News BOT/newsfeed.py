import requests

def get_news(topic):
    url = "https://newsapi.org/v2/everything?"
    topic = 'q=' + topic + '&'
    key = "apiKey=f43e83dd90ba42a6aa79de1d28fb86de"
    
    query = url + topic + key
    
    response = requests.get(query).json()
    articles = response["articles"]
    
    return articles
    