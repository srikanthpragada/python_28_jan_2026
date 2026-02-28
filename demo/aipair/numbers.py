
def isprime(num: int) -> bool:
            """
            Determines if a given number is a prime number.

            A prime number is a number greater than 1 that has no divisors other than 1 and itself.
            This function checks divisibility from 2 up to the square root of the number.

            Args:
                num (int): The number to check for primality.

            Returns:
                bool: True if the number is prime, False otherwise.
            """
            if num < 2:  # Numbers less than 2 are not prime
                return False
            for i in range(2, int(num**0.5) + 1):  # Check divisors up to the square root of the number
                if num % i == 0:  # If divisible by any number, it is not prime
                    return False
            return True  # If no divisors are found, the number is prime


def isperfect(num : int)  -> bool:
    if num < 1:
        return False
    sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_of_divisors == num

