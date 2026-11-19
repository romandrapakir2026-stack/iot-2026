def first_non_consecutive(arr):
    result = None
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            result =  arr[i]
    return result


if __name__ == "__main__":
    arr = [int(x) for x in input("Введіть числа через пробіл:").split()]
    result = first_non_consecutive(arr)
    print(result)
    print(type(arr))