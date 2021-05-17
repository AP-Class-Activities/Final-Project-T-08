def prime(num):
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return True
def MaxFibPrime(num):
    a = 1
    b = 1
    c = 1
    d = 2
    max = 0
    while c < num:
        for i in range(3, d+1):
            c = a+b
            a = b
            b = c
        if c > num:
            return max
        if prime(c) == True:
            max = c
        d = d + 1
    return max
def ABS(num):
    if num >=0:
        return num
    return (ABS(-num))
def COMB(num1, num2):
    return (FAC(num1))//((FAC(num1-num2))*FAC(num2))
def FAC(num):
    if num==1 or num==0:
        return 1
    return FAC(num-1) * num
def LCMS(num1, num2, num3):
    max = num1*num2*num3
    l1 = []
    l2 = []
    l3 = []
    for i in range(1,(max//num1)+1):
        l1.append(num1*i)
    for j in range(1,(max//num2)+1):
        l2.append(num2*j)
    for k in range(1,(max//num3)+1):
        l3.append(num3*k)
    for i1 in range(0, len(l1)):
        for i2 in range(0, len (l2)):
            for i3 in range (0, len (l3)):
                if l1[i1]==l2[i2]==l3[i3]:
                    return l1[i1]
exec(f'print({input()})')
print('hi')