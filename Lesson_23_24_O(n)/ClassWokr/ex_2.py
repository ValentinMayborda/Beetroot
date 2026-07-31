# O(log n) - Логарифмічна складність
def fast_power(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    half = fast_power(base, exponent // 2)

    if exponent % 2 == 0:
        return half * half
    else:
        return base * half * half


print(fast_power(2, 10))  # 2 ^ 10 = 1024
# 10 -> 5 -> 2 -> 1 -> 0