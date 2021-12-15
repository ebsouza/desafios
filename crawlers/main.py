# -*- coding: utf-8 -*-

import argparse

from crawler import IdWallRedditCrawler
from utils import thread_info_to_dict

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--subthreads', dest='subthreads', default=None, type=str,
                    help='Subthreads list as string. Ex: Home;AskReddit;leagueoflegends;Minecraft')
parser.add_argument('--like_threshold', dest='like_threshold', default=0, type=int,
                    help='A threshold to filter threads by votes')
args = parser.parse_args()


for subthread in args.subthreads.split(";"):

    print(f"[Starting scraping: '{subthread}']")

    crawler = IdWallRedditCrawler(subthread, args.like_threshold)
    crawler.run(1)

    print(f"[Finishing scraping: '{subthread}']")

    print("[Results] - Sorted by likes")
    for thread_info in crawler.sorted_threads_info():
        index = crawler.sorted_threads_info().index(thread_info)
        info = thread_info_to_dict(thread_info, index + 1, ["title", "likes", "link", "comments"])
        print(info)
