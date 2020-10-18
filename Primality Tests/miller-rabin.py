import random

number = 67

MAX_TRY_COUNT = 1000
"""
Miller-Rabin test cannot prove the primality %100
"""
def test_miller(count,r, number,s):
    '''
    a : randomly chosen number
    r : odd number
    s : Power of 2
    Returns
    True if number is prime composite
    False if number is composite
    '''
    if count>MAX_TRY_COUNT:
        print("MAX TRY COUNT EXCEED")
        return True
    count+=1
    a = random.randint(1, number-1)
    x = pow(a,r)
    print("Step 1 Cheking , a^r≡±1 mod n -> ","{}^{}≡±1 mod {}".format(a,r,number))
    if x % number == 1 or x % number == number-1:
        print(a," value inappropiate for ",number," Trying step-1 with different a ")
        return test_miller(count,r,number,s) # first congruence holds
    print("Step 2 Checking")
    for i in range(s-1):
        x = pow(a,pow(2,i)*r)
        print("i = {} , a^(2^i*r) -> {}^(2^{}*{}) = {}".format(i,a,i,r,x))
        if x % number  == number -1 :
            print("second congruence does hold for i = {}".format(i))
            print("Trying step-1 with different a")
            return test_miller(count,r, number, s)  # first congruence holds

    return False


def is_prime(number):
    if number<=1: return False
    if number == 2:
        return True
    if number %2 == 0:
        return False

    d = number -1
    s = 0
    while (d % 2 == 0 ):
        d//=2
        s+=1

    return test_miller(1,d,number,s)


if (is_prime(number)):
    print(number, " is prime")
else:
    print(number," is composite")
