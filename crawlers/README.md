## IdWallRedditCrawler

(Description)

### 1. Setup

1. Docker

```
docker build --tag=redditcrawler:idwall .
```

```
docker create -t -i --name idwall_crawler -v <user_workspace>:/home/user redditcrawler:idwall
```

```
docker start idwall_crawler
```

```
docker exec -it idwall_crawler bash
```

2. Local Environment

```
python3 -m venv idwall_crawler
```

```
source idwall_crawler/bin/active
```

```
pip3 install --upgrade pip
```

```
pip install -r requirements.txt
```



### 2. How to scrap old.reddit subreddits

To filter threads up to 500 likes( *--like_threshold* ) on cats and AskReddit subreddits ( *--subreddits*) and send the list to telegram(*--telegram*)

```
python main.py --subreddits cats;AskReddit --like_threshold 500 --telegram
```


