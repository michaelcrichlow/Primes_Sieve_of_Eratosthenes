# Finding the primes less than 100 using the Sieve of Eratosthenes

def remove_common(a: list[int], b: list[int]) -> None:
    """Removes the elements in list 'a' that appear in both lists 'a' and 'b'."""

    for i in a[:]:
        if i in b:
            a.remove(i)

            # this removes the common elements from b
            # which isn't needed at the moment
            # b.remove(i)


def check_if_prime(num: int) -> bool:
    """Returns True if 'num' is prime. Else returns False."""

    is_prime = False
    divisor = num - 1
    exit_loop = False

    while (divisor > 0) and (exit_loop == False):
        if (num % divisor == 0) and (divisor != 1):
            is_prime = False
            exit_loop = True
        elif (num % divisor == 0) and (divisor == 1):
            is_prime = True

        divisor -= 1

    return is_prime


def primes_less_than(num: int) -> list[int]:
    """Returns a list of primes less than 'num'."""

    # create list from 2 to 'num'
    end_num = num + 1
    local_list = list(range(2, end_num))

    # With the values that are in local_list:
    # 1.) check if prime
    for value in local_list:
        if value == 2:
            is_prime = True
        elif value > 2:
            is_prime = check_if_prime(value)

        # 2.) if true, populate new_list with multiples of that number up to end_num
        if is_prime == True:
            new_list = list(range(value*2, end_num, value))

            # 3.) remove the values from local_list that are in both local_list and new_list
            remove_common(local_list, new_list)

            # 4.) with this redefined version of local_list, continue the 'for' loop

    return local_list


def main() -> None:
    # code goes here
    primes_list = primes_less_than(100)
    print(primes_list)


if __name__ == '__main__':
    main()
