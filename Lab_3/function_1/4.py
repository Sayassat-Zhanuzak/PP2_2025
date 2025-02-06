def filter_prime(lst):
    def is_prime(n):
        if n < 2: 
            return False
        
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True

    primes = [nums for nums in lst if is_prime(nums)]
    return primes

user_input = input("Enter elements: ")
numbers = list(map(int, user_input.split())) #list converts iterator that is from map to list
result = filter_prime(numbers)
print(result)