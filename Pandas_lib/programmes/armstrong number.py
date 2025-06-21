n = int(input('enter a number:'))
originalnum = n
sum = 0
while originalnum>0:
    remainder = originalnum%10
    pow = remainder**(len(str(n)))
    sum = sum+pow
    originalnum=originalnum//10

if(sum==n):
    print('Number is armstrong')
else:
    print('Number is not armstrong')