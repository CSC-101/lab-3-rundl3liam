more = [x+1 for x in [1,2,3,4]] #x = 1, 2, 3, 4
print() #more = [2,3,4,5]


def square(n:int) -> int:
    return n * n #n = 1 n = 2, n = 3, n = 4
                # returns 1, 4, 9, 16
squares = [square(x) for x in [1,2,3,4]] #squares is the squared value of whatever x is inputted
print()

def check(n:int) -> bool:
    return n > 2 #0, 1, 2, 3, 4
                #returns false, false, false, true, true


answer = [x for x in range(5) if check(x)] #answer = [3,4]
print()


def inc(m:int) -> int:
    return m + 1  #3, 4
                 #returns 4, 5



def check(n:int) -> bool:
    return n > 2 #0, 1, 2, 3, 4
                #returns false, false, false, true, true

answer = [inc(x) for x in range(5) if check(x)] #answer = [4,5]
print()