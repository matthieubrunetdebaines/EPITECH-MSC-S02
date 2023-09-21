def f ( x ) :
    return 2 * x + 1

def g () :
    return 7

y = f (2)
print ( y )
y = f (5) + g ()
print ( y )

# this piece of code is composed by 2 functions
# function f multiplies the argument by 2 and add 1
# function g returns 7

# first variable stocks 2*2+1 = 5
# second variable stocks 5*2+1 + 7 = 18


