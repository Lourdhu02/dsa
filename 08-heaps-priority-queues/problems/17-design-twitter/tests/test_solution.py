from solution import Twitter


def test_classic_flow():
    t = Twitter()
    t.post_tweet(1, 5)
    assert t.get_news_feed(1) == [5]
    t.follow(1, 2)
    t.post_tweet(2, 6)
    assert t.get_news_feed(1) == [6, 5]
    t.unfollow(1, 2)
    assert t.get_news_feed(1) == [5]
