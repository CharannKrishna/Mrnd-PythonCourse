'''
Given a string of digits, you must return a list of all (substring, count) in the input string such that count >=2 and 
len(substring) >= 2. count represents the number of times the substring repeats in the input string (non-overlapping 
occurances).

The result must be sorted by count first (descending) and then in case of a tie the numerical value of 
substring (descending)

For e.g. if input is "123451236786712" you must return [("12", 3), ("123", 2), ("67", 2), ("23", 2)]

Notes:
1. if input is not a str, raise TypeError
2. Write clean bruteforce code to do this using python features. Do not devise new algorithms in the exam!
3. Write your own test cases 
'''




def repeats(digits):
    if not isinstance(digits,str):
        raise TypeError
    d=dict()
    for i in range(2,len(digits)+1):
        for j in range(len(digits)-i+1):

            k=digits[j:j+i]
            v=digits.count(k)
            if v>=2:
                d[k]=v
    res=d.items()
    res=sorted(res,key=lambda a:int(a[0]),reverse=True)
    res=sorted(res,key=lambda a:a[1],reverse=True)
    return res


def test_repeats():
    assert [("12", 3), ("123", 2), ("67", 2), ("23",2)] == repeats("123451236786712")
