# -*- coding:utf-8 -*-

#これは最小公倍数
limit = 21
values = []
for i in range(1, limit):
    values.append(i)

x = 1
for i in values:
    x *= i

y = 2
primeFactors = []
while True:
    if x % y == 0:
        primeFactors.append(y)
        x = x / y
    else:
        y += 1
    if x == 1:
        break
uniqFactor = list(set(primeFactors))
print(uniqFactor)
s=1
for i in uniqFactor:
    s *= i

saisyouKoubaisuu = s
#print(s)



