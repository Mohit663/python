import math

year=int(input('enter the year : '))

# Square root of the year
sqrt=float(math.isqrt(year))
is_square=sqrt*sqrt==year
if(is_square):
    print('The',year,'year is a perfect square')
else:
    print('The',year,'year is not a perfect square')
print('The square root of the year is : ',sqrt)

# Triangular number check
# if(is_square):
#     n=sqrt
#     x=((n)*(n+1))/2

# Product of Two Squares


# Sum of Three Squares


# Five Times Table
FTT=year/5
if(year%5==0):
    print('The year comes in five times table')
else:
    print('The year not comes in five times table')
print(FTT)
