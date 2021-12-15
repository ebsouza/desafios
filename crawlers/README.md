## IdWallRedditCrawler

![](assets/idwall_crawler.gif)

### 1. Setup

1. Local Environment

```
python3 -m venv idwall_crawler
```

```
source idwall_crawler/bin/active
```

```
(idwall_crawler) pip install --upgrade pip
```

```
(idwall_crawler) pip install -r requirements.txt
```

2. Docker

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
docker exec -it idwall_crawler bash -c "python3 main.py --subreddits cats --like_threshold 500"
```


### 2. Scraping old.reddit subreddits

Filtering threads over 500 likes( *--like_threshold* ) on cats and AskReddit subreddits ( *--subreddits*) and send that via telegram(*--telegram*)

```
# Local environment
python main.py --subreddits 'cats;AskReddit' --like_threshold 500 --telegram
```

```
# Docker
docker start idwall_crawler
docker exec -it idwall_crawler bash -c "python3 main.py --subreddits 'cats;AskReddit' --like_threshold 500" --telegram
```

