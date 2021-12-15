## IdWallRedditCrawler

(Description)

### 1. Setup

1. Docker


2. Local Environment


### 2. How to scrap old.reddit subreddits

To filter threads up to 500 likes( *--like_threshold* ) on cats and AskReddit subreddits ( *--subreddits*) and send the list to telegram(*--telegram*)

```
python main.py --subreddits cats;AskReddit --like_threshold 500 --telegram
```


