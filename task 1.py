more = [x + 1 for x in [1,2,3,4]]     # x=2,x=3,x=4,x=5
print()                               # [2,3,4,5]

def square(n:int) -> int:
    return n * n                           # n=1,n=2,n=3,n=4
                                           # 1,4,9,16


squares = [square(x) for x in [1,2,3,4]]   # [1,4,9,16]
print(squares)               # this squares each value in the list and makes a new one with those values


def check(n:int) -> bool:
    return n > 2                             # n=0,n=1,n=2,n=3,n=4
                                             # false,false,false,true,true


answer = [x for x in range(5) if check(x)]   # [3,4]
print()

def inc(m:int) -> int:
    return m + 1                             # m=0,m=1,m=2,m=3,m=4
                                             # 1,2,3,4,5


def check(n:int) -> bool:
    return n > 2                             # n=0,n=1,n=2,n=3,n=4
                                             # false,false,false,true,true


answer = [inc(x) for x in range(5) if check(x)]   # [4,5]
print(answer)
