# -*- coding:utf-8 -*-
if __name__ == "__main__":
    x = 600851475143
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
    #uniqFactor = list(set(primeFactors))
    #print(uniqFactor)
    print(max(primeFactors))
