import math
print("\nThe Prime numbers between 1 to 500 are: \n")
primes_using_loop = []
for i in range(2, 501):
    for j in range(2, int(math.sqrt(i)+2)):
        is_prime = True
        if(i==j):
            break
        if i%j == 0:
            is_prime = False
            break
    if(is_prime == True):
        primes_using_loop.append(i)
print(primes_using_loop)

#primes_using_list_c = [i for i in range(2, 501) if i=None and break if(i%j == 0) for j in range(2, int(math.sqrt(i)+2)))]