def solution(s: str, k: int) -> int:
    start, end = 0, k
    max_len = k

    while end <= len(s):
        if len(set(s[start:end])) <= k:
            current_len = end - start

            if current_len > max_len:
                max_len = current_len

            end += 1
        else:
            start += 1

    return max_len

print(solution('abcba', 2))