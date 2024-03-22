import requests
API_KEY = " "
URL = ("https://newsapi.org/v2/top-headlines?")


def get_by_topHeadlines(category):
    query_parameters = {
        "apiKey": API_KEY,
        "category": category,
        "country": "in"
    }
    return get_articles(query_parameters)


def get_articles(params):
    r = requests.get(URL, params)
    articles = r.json()['articles']

    results =[]
    for article in articles:
        results.append({'title':article['title'], 'url': article['url'],'content':article['content']})

    for result in results:
        print(result['title'])
        print(result['content'])
        print(result['url'])
        print(" ")


if __name__ == "__main__":
    get_by_topHeadlines("health")

