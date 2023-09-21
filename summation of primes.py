# This algorithm to find sum of primes becomes really slow when the range is huge.
b = []  # to store list of boolean values(t/f) depending on a number having no perfect divisors but 1 and itself.
a = 0
for j in range(2, 2000000):
    for i in range(2, j):
        if j % i != 0:
            b.append(False)

        else:
            b.append(True)
            break  # to make our code run faster, by breaking if a number has a perfect divisor.
    if all(f == False for f in b):  # if b has all false values then it means it is a prime with no perfect divisors.
        # print(j) was added to code to see if it is working(it prints the primes values)
        a = a + j
    b.clear()
print("sum of primes is", a)

