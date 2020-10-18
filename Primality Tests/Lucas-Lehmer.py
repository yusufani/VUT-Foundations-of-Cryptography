number = 29


def lucas_lehmer(number):
    val = number+1
    s = 0
    while (val != 1):
        if val % 2 == 0:
            val /= 2
            s += 1
        else:
            print("Number is not appropriate for lucas-lehmer test."
                  "The number has to be in (2^n -1) form  ")
            break
    if val == 1:
        u=4
        print("U0 = 4")
        for i in range(3):
            u = (u*u - 2) % number
            print("U{} = {}".format(i+1,u))
        if u == 0 :
            print(number," is prime")
        else:
            print(number," is not prime")


lucas_lehmer(63)