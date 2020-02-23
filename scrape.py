import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hack_news_list):
    """sort votes(points) of each article

    Args:
        hack_news_list (list): list of hack news web site feed

    Returns:
        list: dictionary list sorted by votes
    """
    # Common pattern with sorted function
    return sorted(hack_news_list, key=lambda k: k['vote'], reverse=True)


def create_custom_hn(links, subtext):
    """[summary]

    Args:
        links (list): list of links
        votes (list): list of users votes called points on website
    """
    hack_news = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hack_news.append(
                    {'title': title, 'link': href, 'vote': points})
    return sort_stories_by_votes(hack_news)


pprint.pprint(create_custom_hn(links, subtext))
