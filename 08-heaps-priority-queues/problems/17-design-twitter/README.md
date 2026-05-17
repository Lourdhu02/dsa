# 17. Design Twitter feed  `[medium]`

Implement `Twitter` with `post_tweet(user_id, tweet_id)`, `get_news_feed(user_id) -> list[int]` (10 most recent tweets from the user + followees, newest first), `follow(a, b)`, `unfollow(a, b)`.

## Function signature

```python
class Twitter:
    def post_tweet(self, user_id: int, tweet_id: int) -> None: ...
    def get_news_feed(self, user_id: int) -> list[int]: ...
    def follow(self, a: int, b: int) -> None: ...
    def unfollow(self, a: int, b: int) -> None: ...
```

## Examples

```
t = Twitter()
t.post_tweet(1, 5)
t.get_news_feed(1)   # [5]
t.follow(1, 2)
t.post_tweet(2, 6)
t.get_news_feed(1)   # [6, 5]
t.unfollow(1, 2)
t.get_news_feed(1)   # [5]
```



## Hint

<details>
<summary>Hint</summary>

Per-user list of (timestamp, tweet_id). Get_feed: merge user's + followees' streams with a heap, take 10.
</details>
