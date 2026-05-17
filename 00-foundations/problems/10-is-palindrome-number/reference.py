def is_palindrome_number(n: int) -> bool:
    """Compare digits without using string conversion.

    We reverse only *half* the digits so we don't have to worry about
    overflow in fixed-width integer settings (Python doesn't overflow, but
    this is the technique people port to C++/Java).

    Time:  Θ(d) where d = number of digits.
    Space: Θ(1).
    """
    if n < 0:
        return False
    if n != 0 and n % 10 == 0:
        return False  # non-zero trailing zero can't be palindrome.
    reversed_half = 0
    while n > reversed_half:
        reversed_half = reversed_half * 10 + n % 10
        n //= 10
    # Odd-length palindromes leave one extra digit in reversed_half; drop it.
    return n == reversed_half or n == reversed_half // 10
