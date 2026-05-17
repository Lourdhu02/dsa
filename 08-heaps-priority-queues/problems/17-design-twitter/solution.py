class Twitter:
    def __init__(self) -> None:
        raise NotImplementedError

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        raise NotImplementedError

    def get_news_feed(self, user_id: int) -> list[int]:
        raise NotImplementedError

    def follow(self, a: int, b: int) -> None:
        raise NotImplementedError

    def unfollow(self, a: int, b: int) -> None:
        raise NotImplementedError
