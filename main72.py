def rotate(arr: list, k: int) -> None:

    if len(arr) == k:
        return

    n: int = len(arr) - k

    for i in range(n):

        arr.insert(0, None)

    for i in range(n - 1, -1, -1):

        arr[len(arr) + i - n], arr[i] = arr[i], arr[len(arr) + i - n]

    for i in range(n - 1, -1, -1):

        arr.pop(len(arr) - i - 1)

numbers: list = [1, 2, 3, 4, 5, 6, 7]

rotate(numbers, 5)

print(numbers)