# WRITE YOUR SOLUTION HERE:
def remove_smaller_than(numbers: list, limit: int):
    return [number for number in numbers if number >= limit]


if __name__ == "__main__":
    print(remove_smaller_than([1, 2, 3, 4, 5, 6, 7], 4))
    print(remove_smaller_than([100, 101, 102, 105, 106, 103, 99, 98, 107], 105))

    