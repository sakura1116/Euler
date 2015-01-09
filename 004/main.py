# -*- coding:utf-8 -*-

def isKaibun(param):
    h = int(len(param) / 2)
    for a, b in zip(param, reversed(param)):
        #print(a, b)
        if a != b:
            return False
    return True

if __name__ == "__main__":
    x = 999 * 999
    while True:
        is_kaibun = isKaibun(list(str(x)))
        if is_kaibun == True:
            break
        x -= 1
    print(x)
