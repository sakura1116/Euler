# -*- coding:utf-8 -*-
if __name__ == "__main__":
    result, x, y = 0, 0, 1
    while y < 4000000:
        if y % 2 == 0:
            result += y
        x, y =  y, x + y
    print(result)
