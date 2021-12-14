# -*- coding: utf-8 -*-

import argparse

from crawler import IdWallRedditCrawler
from utils import print_threads

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--subthreads', dest='subthreads', default=None, type=str,
                    help='Subthreads list as string. Ex: Home;AskReddit;leagueoflegends;Minecraft')
parser.add_argument('--vote_threshold', dest='vote_threshold', default=0, type=int,
                    help='A threshold to filter threads by votes')
args = parser.parse_args()


for subthread in args.subthreads.split(";"):

    print(f"[Starting scraping: '{subthread}']")

    crawler = IdWallRedditCrawler(subthread, args.vote_threshold)
    crawler.run()

    print(f"[Finishing scraping: '{subthread}']")

    print("[Results] - Sorted by likes")
    print_threads(crawler.sorted_threads_info(), ["title", "likes", "link", "comments"])
    #print_threads(crawler.threads[:10], ["title", "likes", "link", "comments"])


