import heapq
from collections import defaultdict


class Twitter:
    def __init__(self) -> None:
        self._tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self._follow: dict[int, set[int]] = defaultdict(set)
        self._t = 0

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self._t += 1
        self._tweets[user_id].append((self._t, tweet_id))

    def get_news_feed(self, user_id: int) -> list[int]:
        users = self._follow[user_id] | {user_id}
        h: list[tuple[int, int]] = []  # (-timestamp, tweet_id)
        for u in users:
            for t, tid in self._tweets[u][-10:]:
                heapq.heappush(h, (-t, tid))
        out: list[int] = []
        for _ in range(10):
            if not h:
                break
            out.append(heapq.heappop(h)[1])
        return out

    def follow(self, a: int, b: int) -> None:
        if a != b:
            self._follow[a].add(b)

    def unfollow(self, a: int, b: int) -> None:
        self._follow[a].discard(b)
