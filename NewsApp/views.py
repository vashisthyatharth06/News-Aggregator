from django.shortcuts import render
from newsapi import NewsApiClient



def index(request):
    newsapi = NewsApiClient(api_key="b044fdb99af34abbadb6c51f7e842a8f")
    #India News(Times Of India)
    topheadlines_toi = newsapi.get_top_headlines(sources='the-times-of-india')


    articles_toi = topheadlines_toi['articles']

    desc_toi = []
    news_toi = []
    img_toi = []
    links_toi=[]

    for i in range(len(articles_toi)):
        myarticles_toi = articles_toi[i]

        news_toi.append(myarticles_toi['title'])
        desc_toi.append(myarticles_toi['description'])
        img_toi.append(myarticles_toi['urlToImage'])
        links_toi.append(myarticles_toi['url'])


    mylist_toi = zip(news_toi, desc_toi, img_toi, links_toi)

    #World News(BBC NEWS)
    topheadlines_bbc = newsapi.get_top_headlines(sources='bbc-news')
    articles_bbc = topheadlines_bbc['articles']

    desc_bbc = []
    news_bbc = []
    img_bbc= []
    links_bbc=[]

    for i in range(len(articles_bbc)):
        myarticles_bbc = articles_bbc[i]

        news_bbc.append(myarticles_bbc['title'])
        desc_bbc.append(myarticles_bbc['description'])
        img_bbc.append(myarticles_bbc['urlToImage'])
        links_bbc.append(myarticles_bbc['url'])


    mylist_bbc = zip(news_bbc, desc_bbc, img_bbc, links_bbc)


    return render(request, 'index.html', context={"mylist_toi":mylist_toi,"mylist_bbc":mylist_bbc})



