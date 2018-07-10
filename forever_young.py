#import time
import unittest

def dec(num, base):
    exp=0
    d=0
    for i in num:
        d+=(base**exp)*int(i)
        exp+=1
    return d

def enc(d, base):
    r=[]
    while d>0:
        r.append(str(d%base))
        d//=base
    return r
  
def base_search(d, num):
    a=10
    b=d-1
    m=(a+b)/2
    r=0
    while a!=m and m!=b and r==0:
        e1=dec(num, a)
        e2=dec(num, m)
        e3=dec(num, b)
        if e1==d:
            r=a
        elif e2==d:
            r=m
        elif e3==d:
            r=b
        elif d<e2:
            b=m
        elif e2<d:
            a=m
        m=(a+b)/2
    return r

def forever(age, low):
    for i in range(low,10001):
        ii=list(str(i)[::-1])
        if i==10000:
            return "end"
        if base_search(age,ii)!=0:
            return base_search(age,ii)

def young(age):
    for b in range(100000,9,-1):
        num=enc(age,b)
        check=1
        for i in num:
            if int(i)>9:
                check=0
                break
        if check:
            return b

def forever_young(age,low):
    if low>10000:
        return young(age)
    else:
        r=forever(age,low)
        if r=="end":
            return young(age)
        else:
            return r

#while True:
#    o=raw_input('age low: ')
#    f=o.split(' ')
#    start_time = time.clock()
#    print forever_young(int(f[0]),int(f[1]))
#    print ("--- %s seconds ---" % (time.clock() - start_time))

#print dec([5,5,9,7,8,6,5,4,3],34)

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(forever_young(32,20), 16)
        #self.assertEqual(forever_young(2016,100), 42)
        #self.assertEqual(forever_young(55,35), 16)
        #self.assertEqual(forever_young(417,200), 13)
        #self.assertEqual(forever_young(2031,363), 25)
        #self.assertEqual(forever_young(65348348552974,125),11)

if __name__ == '__main__':
    unittest.main()
