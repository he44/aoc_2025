import sys
from typing import Optional

# Odd number of digits -> None
# Even number of digits (2 * n) -> 10 ** n + 1
# E.g. 1212 = 101 * 12, 234234 = 1001 * 234
def get_invalid_pattern(num_digits: int) -> Optional[int]:
    if num_digits % 2 or num_digits == 0:
        return None
    return 10 ** (num_digits // 2) + 1


def get_num_digits(num: int) -> int:
    return len(str(num))


def get_sum_of_all_invalid_ids_with_length_n(num_digits: int) -> int:
    if num_digits % 2 or num_digits == 0:
        return 0
    pattern = get_invalid_pattern(num_digits)
    minimal = 10 ** (n - 1)
    maximal = 10 ** n - 1
    # min = 1000, max = 9999,
    # Loop i from 10 (1010), to 99 (right bound needs to be last + 1)
    sum = 0
    for i in range(minimal // pattern + 1, maximal // pattern + 1):
        sum += i * pattern
    return sum

def get_sum_of_all_invalid_ids_between_2_numbers_of_same_length(left: int, right: int) -> int:
    assert len(str(left)) == len(str(right)), f"{left} v.s. {right}"
    num_digits = len(str(left))
    pattern = get_invalid_pattern(num_digits)
    if pattern is None:
        return 0
    sum = 0
    for i in range(left // pattern, right // pattern + 2):
        if i * pattern >= left and i * pattern <= right:
            sum += i * pattern
    return sum

def get_sum_of_invalid_ids(left: int, right: int) -> int:
    num_digits_low = get_num_digits(left)
    num_digits_high = get_num_digits(right)
    sum = 0
    # Simple case
    if (num_digits_low == num_digits_high):
        return get_sum_of_all_invalid_ids_between_2_numbers_of_same_length(left, right)

    # Complex case
    # Summing over all from `left` to 10 ** (num_digits_low + 1) - 1
    sum += get_sum_of_all_invalid_ids_between_2_numbers_of_same_length(left, 10 ** num_digits_low  - 1)
    # Summing over all in between
    for n in range(num_digits_low + 1, num_digits_high):
        sum += get_sum_of_all_invalid_ids_with_length_n(n)
    # Summin gover all from 10 ** (num_digits_high - 1) to `right`
    sum += get_sum_of_all_invalid_ids_between_2_numbers_of_same_length(10 ** (num_digits_high - 1), right)
    return sum


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()[0]
    ans = 0
    for content in contents.split(","):
        line = content.strip()
        left, right = line.split("-")
        left = int(left)
        right = int(right)
        ans += get_sum_of_invalid_ids(left, right)
    print(ans)

if __name__ == "__main__":
    main()
