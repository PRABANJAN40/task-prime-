def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_primes(start, end):
    if start > end:
        print("Enter the correct range")
        return []

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
start=int(input("Enter start value: "))
end=int(input("Enter end value: "))
print(find_primes(start,end))
