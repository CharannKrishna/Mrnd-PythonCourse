'''
A magic number is a number which results in 1 when the following process is done.

1. replace number with sum of squares of each digit (the result should be converted to same base)
2. repeat till you get a single digit

If result is 1, then it is a magic number, else it is not.

e.g. 28  is a magic number in base 10.
28 -> 68 ( 4 + 64) -> 100 (36 + 64) -> 1

12 is not a magic number in base 10
12 -> 5 ( 1 + 4)

12 is not a magic number is base 5
22 (12 in base 10 is 22 in base 5)
-> 13 (4 + 4 = 8 in base 5 is 13)
-> 20 (1 + 9 = 10 in base 5 is 20) ->
-> 4 (single digit and it is not 1, so not a magic number).

18 is a magic number in base 8

22 (18 in base 10 is 22 in base 8)
-> 10 ( 4+ 4 = 8 which is 10 in base 8)
-> 1 (single digit and it is 1, so it is a magic number)

Your job for this question is to write a couple of routines to find the first K magic numbers in base 8 in ascending order.

Notes:
1. k < 0 should raise ValueError.
2. Fill up the two routines below to get the job done. The 2nd method should call the first in a loop till
   it gets the 1st k magic numbers.
3. Use python builtins and data structures to solve this problem.
4. Use the debugger or pytutor or add prints if you get stuck :).
5. Note that both routines will be tested independently, so do not rename the methods or write all the logic in 
   get_oct_magic_numbers method.
'''

# Given a number, returns True if it is a magic number is base 8, else False
# raise ValueError if number < 0
def is_oct_magic(number):
    if number<0:
        raise ValueError
    number=oct(number)[2:]
    number=str(number)
    while len(number)>1:
        s=0
        for i in number:
            s=s+(int(i)**2)
        number=oct(s)[2:]
    if number=='1':
        return True
    else:
        return False

# This method makes use of is_oct_magic and returns a list of 1st k magic numbers in base 8
def get_oct_magic_numbers(k):
    if k<0:
        raise ValueError
    count=k
    number=1
    res=[]
    while count:
        if is_oct_magic(number):
            res.append(number)
            count-=1
        number+=1
    return res


# some basic tests given, write more according to given constraints. atleast check that
# you can generate 10 magic numbers

def test_is_oct_magic():
    assert is_oct_magic(7) == False
    assert is_oct_magic(1) == True
    assert is_oct_magic(18) == True

def test_get_oct_magic_numbers():
    assert [1, 8] == get_oct_magic_numbers(2)
