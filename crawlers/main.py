# -*- coding: utf-8 -*-

import argparse

from crawler import IdWallRedditCrawler
from utils import thread_info_to_string
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

    try:
        crawler = IdWallRedditCrawler(subreddit, args.like_threshold)
        crawler.run()
    except Exception as e:
        print(f"Sorry. It was not possible run the crawler. Reason : {e}")
        continue

    print(f"[Finishing scraping: '{subreddit}']")

    print("[Results] - Sorted by likes")
    for thread_info in crawler.sorted_threads_info():
        index = crawler.sorted_threads_info().index(thread_info)
        thread_info_str = thread_info_to_string(thread_info, index + 1, ["title", "likes", "link", "comments"])
        try:
            print(thread_info_str)
        except UnicodeEncodeError:
            print("Invalid character!")

        if args.telegram:
            telegram_client.send_message(phone, thread_info_str)
