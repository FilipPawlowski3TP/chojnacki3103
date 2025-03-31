def nwd(a, b):
    if a == b:
        return a
    else:
        if a > b:
            a = a - b
            return nwd(a, b)
        else:
            b = b - a
            return nwd(a, b)


liczba1 = 124
liczba2 = 8
print(nwd(liczba1, liczba2))

def nwd2(a, b):
    while b != 0:
        n=b
        b = a % b
        a = n
    else:
        return a


liczba3=124
liczba4=8
print(nwd2(liczba3, liczba4))

import math
a=[]
def wypelnij(tablica):
    for i in range(101):
        tablica.append(True)
wypelnij(a)
n=100
for i in range(2,int(math.sqrt(n))+1):
    if a[i] == True:
        for j in range(2*i,n+1,i):
            a[j] = False


for i in range(2,n+1):
    if a[i] == True:
        print(i, end=", ")

