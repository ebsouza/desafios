# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from utils import concatenate_link


class IdWallRedditCrawler:

    base_url = 'https://old.reddit.com/'

    def __init__(self, subthread, vote_threshold=0):
        self.threads = list()
        self.url = f"{self.base_url}r/{subthread}/"
        self.vote_threshold = vote_threshold

    def run(self, page_limit=1000):
        page_generator = self.next_page_generator()
        url = next(page_generator)
        response = self.request(url)

        count_pages = 0

        while response.status_code == 200:
            all_elements = self.__extract_parent_element(response.content)
            if not all_elements:
                break

            count_pages += 1
            print(f"Scraping page : {count_pages}")

            for element in all_elements.contents:
                try:
                    info = self.__extract_info(element)
                    self.__update_subthread_list(info)
                except TypeError as e:
                    pass

            else:
                next_url = next(page_generator)
                next_url += f"&after={info['id']}"
                response = self.request(next_url)

            if count_pages >= page_limit:
                break

    def sorted_threads_info(self):
        from operator import itemgetter
        return sorted(self.threads, key=itemgetter("likes"), reverse=True)

    def next_page_generator(self):
        yield self.url
        count = 0
        while True:
            count += 25
            yield f"{self.url}?count={count}"

    def request(self, url):
        browser_data = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" + \
                       "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        headers = {"User-Agent": browser_data}

        return requests.get(url, headers=headers)

    def __extract_parent_element(self, html_page):
        soup = BeautifulSoup(html_page, 'html.parser')
        parent_element = soup.find("div", {"id": "siteTable"})

        if len(parent_element) == 1:
            return None

        return parent_element

    def __extract_info(self, html_element):
        info = dict()

        info['id'] = html_element.get('data-fullname')
        if not info['id']:
            raise TypeError("There is no data-fullname field")

        info['likes'] = self.__extract_votes(html_element)
        info['title'], info['link'], info['comments'] = self.__extract_thread(html_element)

        return info

    def __extract_votes(self, html_element):
        votes = html_element.find("div", {"class": "midcol unvoted"})
        likes = votes.find("div", {"class": "score likes"}).get('title')
        return int(likes)

    def __extract_thread(self, html_element):
        thread = html_element.find("div", {"class": "entry unvoted"})
        title = thread.find("a", {"data-event-action": "title"}).text
        link = thread.find("a", {"data-event-action": "title"}).get('href')
        link = concatenate_link(self.base_url, link)
        try:
            comments = thread.find("a", {"data-event-action": "comments"}).get('href')
        except AttributeError as e:
            comments = "<<No comments>>"

        return title, link, comments

    def __update_subthread_list(self, subthread_info):
        votes = subthread_info["likes"]
        if votes >= self.vote_threshold:
            self.threads.append(subthread_info)
