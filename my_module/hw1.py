import unittest

def test1(i):
    ans = ""
    for j in range(3):
        if i > 0:
            ans += "大於0"
            i-=1
        elif i < 0:
            ans += "小於0"
            i+=1 
        else:
            ans += "等於0"
            i+=1
    return ans           