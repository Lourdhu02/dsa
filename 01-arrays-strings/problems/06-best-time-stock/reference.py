def max_profit(prices: list[int]) -> int:
    """Single pass with running minimum.

    Invariant: at the top of iteration i, ``min_price == min(prices[0..i-1])``
    and ``best == max profit achievable selling on or before day i-1``.

    Time:  Θ(n)
    Space: Θ(1)
    """
    if not prices:
        return 0
    min_price = prices[0]
    best = 0
    for p in prices[1:]:
        if p < min_price:
            min_price = p
        elif p - min_price > best:
            best = p - min_price
    return best
