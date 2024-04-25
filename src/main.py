def main():
    print('Hello, World!')


if __name__ == '__main__':
    main()

import random


def sort_list(rand_list):
    n = len(rand_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if rand_list[j] > rand_list[j + 1]:
                rand_list[j], rand_list[j + 1] = rand_list[j + 1], rand_list[j]
    return rand_list


def avg_odd_even_numb(rand_list):
    sum_even = 0
    count_even = 0
    sum_odd = 0
    count_odd = 0

    for num in rand_list:
        if num % 2 == 0:  # Check if the number is even
            sum_even += num
            count_even += 1
        else:  # Number is odd
            sum_odd += num
            count_odd += 1

    # Calculate average for even and odd numbers

    try:
        avg_even = sum_even / count_even
    except ZeroDivisionError:
        avg_even = 0

    try:
        avg_odd = sum_odd / count_odd
    except ZeroDivisionError:
        avg_odd = 0

    print(f"Average even number: {avg_even}")
    print(f"Average odd number: {avg_odd}")


# Generate a list of 100 random numbers between 0 and 1000
rand_numb_list = [random.randint(0, 1000) for _ in range(100)]
print(f'List with 100 random numbers:  {rand_numb_list}')
sorted_rand_numb = sort_list(rand_numb_list)
print(f'Sorted list:  {sorted_rand_numb}')
avg_odd_even_numb(rand_numb_list)
