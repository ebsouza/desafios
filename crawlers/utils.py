import requests
from bs4 import BeautifulSoup


def extract_parent_element(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')

    parent_element = soup.find("div", {"id": "siteTable"})

    if len(parent_element) == 1:
        return None

    return parent_element


def extract_info(html_element):
    info = dict()

    info['id'] = html_element.get('data-fullname')
    if not info['id']:
        raise Exception("There is no data-fullname field")

    info['likes'], info['dislikes'], info['unvoted'] = extract_votes(html_element)
    info['title'], info['link'] = extract_thread(html_element)

    return info


def extract_votes(html_element):
    votes = html_element.find("div", {"class": "midcol unvoted"})
    try:
        likes = votes.find("div", {"class": "score likes"}).text
        likes = int(likes)
    except AttributeError:
        likes = 0

    try:
        dislikes = votes.find("div", {"class": "score dislikes"}).text
        dislikes = int(dislikes)
    except AttributeError:
        dislikes = 0

    try:
        unvoted = votes.find("div", {"class": "score unvoted"}).text
        unvoted = int(unvoted)
    except AttributeError:
        unvoted = 0

    return likes, dislikes, unvoted


def extract_thread(html_element):
    thread = html_element.find("div", {"class": "entry unvoted"})
    title = thread.find("a", {"data-event-action": "title"}).text
    link = thread.find("a", {"data-event-action": "title"}).get('href')

    return title, link


def next_base_url(base_url):
    yield base_url
    count = 0
    while True:
        count += 25
        yield f"{base_url}?count={count}"


def do_request(url):
    browser_data = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" + \
                   "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    headers = {"User-Agent": browser_data}

    return requests.get(url, headers=headers)


def sort_info_list(info_list):
    from operator import itemgetter
    return sorted(info_list, key=itemgetter('unvoted'), reverse=True)
