__author__ = 'Kalyan'

notes = '''
These are the kind of questions that are typically asked in written screening tests by companies,
so treat this as practice!

Convert the passed in positive integer number into its prime factorization form.

If number = a1 ^ p1 * a2 ^ p2 ... where a1, a2 are primes and p1, p2 are powers >=1 then we represent that using lists
and tuples in python as [(a1,p1), (a2,p2), ...]

Note that a1 < a2 < ... and p1, p2 etc are all >= 1.

For e.g.
 [(2,1), (5,1)] is the correct prime factorization of 10 as defined above.
 [(5,1), (2,1)] is invalid as the the order is not correct.
 [(2,1), (3,0), (5,1)] is invalid as a prime with power 0 is present in the result.

Notes
0. This problems asks for explicit type checking!
1. Corner case 1 is represented as an empty list: []
2. Non positive numbers should raise a ValueError
3. If the type of number is not int raise a TypeError

Write simple brute force code. No need to write code for generating primes etc.
'''
import math
def primes(num):
    res=[]
    for num in range(2, num+1):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            res.append(num)
    return res

def factorize_number(number):
    if number<0:
        raise ValueError
    if not isinstance(number,int):
        raise TypeError
    result={}
    j=2
    while number>1:
        for i in range(j,int(math.sqrt(number+0.05))+1):
            if number%i==0:
                number=number/i
                j=i
                if i in result:
                    result[i]+=1
                else:
                    result[i]=1
                break
        else:
            if number>1:
                if number in result:
                    result[number]+=1
                else:
                    result[number]=1
                break

    return list(zip(result.keys(),result.values()))

# you are given the tests here according to the spec, usually you will have to write these yourself from the spec!
def test_factorize_number():
    assert [] == factorize_number(1)
    assert [(2, 1)] == factorize_number(2)
    assert [(2, 1), (5, 1), (601, 1)] == factorize_number(6010)
    assert [(5, 2), (7, 1)] == factorize_number(175)
    assert [(2, 1), (7919, 4)] == factorize_number(7865228921869442)
    try:
        factorize_number(-3)
        assert False, "negative number did not throw"
    except ValueError as ve:
        pass

    try:
        factorize_number(2.3)
        assert False, "float did not throw"
    except TypeError as te:
        pass
