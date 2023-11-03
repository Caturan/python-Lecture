
#Write the sum_of_digits function which  satisfies the tests given below.

def sum_of_digits(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    n = abs(n)  # Make the number non-negative

    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10

    return digit_sum

if __name__ == "__main__":
    tests = [[1, 1], [23, 5], [1001, 2], [5623, 16]]
    for x in tests:
        result = sum_of_digits(x[0])
        if result != x[1]:
            print(f"Value test failed for {x[0]}. Expected {x[1]}, got {result}")

    type_tests = [1.5, 1 + 2j, "a", True]
    for x in type_tests:
        try:
            result = sum_of_digits(x)
            print(f"Type test failed for {x}. Result: {result}")
        except TypeError as e:
            print(f"Type test passed for {x}. Raised an exception: {e}")

    print("Tests are completed")


