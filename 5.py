def solution(n):
    num = int(n)
    counts = []
    
    dive(num, 0, counts)

    return min(counts)


def dive(n, currentCount, counts):
    if len(counts) > 0 and currentCount >= min(counts):
        return

    if n == 1:
        counts.append(currentCount)
        return

    return [dive(n / 2 if n % 2 == 0 else n + 1, currentCount + 1, counts),
            dive(n / 2 if n % 2 == 0 else n - 1, currentCount + 1, counts)]


# print(solution('15'))
# print(solution('4'))
print(solution('199'))