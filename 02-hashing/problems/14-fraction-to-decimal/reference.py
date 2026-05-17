def fraction_to_decimal(numerator: int, denominator: int) -> str:
    """Long division with remainder-seen map.

    Time:  Θ(d) where d is the period length (bounded by denominator).
    Space: Θ(d).
    """
    if numerator == 0:
        return "0"
    sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
    n, d = abs(numerator), abs(denominator)
    integer, rem = divmod(n, d)
    if rem == 0:
        return sign + str(integer)
    out = [sign, str(integer), "."]
    seen: dict[int, int] = {}
    while rem and rem not in seen:
        seen[rem] = len(out)
        rem *= 10
        digit, rem = divmod(rem, d)
        out.append(str(digit))
    if rem:
        i = seen[rem]
        out.insert(i, "(")
        out.append(")")
    return "".join(out)
