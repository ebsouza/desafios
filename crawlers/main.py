# -*- coding: utf-8 -*-

import argparse

from crawler import IdWallRedditCrawler
from utils import thread_info_to_dict
from telegram_robot import TelegramMessager

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--subreddits', dest='subreddits', default=None, type=str,
                    help='Subthreads list as string. Ex: Home;AskReddit;leagueoflegends;Minecraft')
parser.add_argument('--like_threshold', dest='like_threshold', default=0, type=int,
                    help='A threshold to filter threads by votes')
parser.add_argument('--telegram', dest='telegram', action='store_true',
                    help='sum the integers (default: find the max)')
args = parser.parse_args()

if args.telegram:
    phone = "+5524999141414"
    telegram_client = TelegramMessager()

for subreddit in args.subreddits.split(";"):

    print(f"[Starting scraping: '{subreddit}']")
    crawler = IdWallRedditCrawler(subreddit, args.like_threshold)
    crawler.run(1)
    print(f"[Finishing scraping: '{subreddit}']")

    print("[Results] - Sorted by likes")
    for thread_info in crawler.sorted_threads_info():
        index = crawler.sorted_threads_info().index(thread_info)
        info = thread_info_to_dict(thread_info, index + 1, ["title", "likes", "link", "comments"])
        print(info)

        if args.telegram:
            telegram_client.send_message(phone, info)
