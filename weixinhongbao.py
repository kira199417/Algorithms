# -*- coding: utf-8 -*-
import random
import sys
 
def randBonus(min, max, total,num):
    print min, max, total, num 
    #print "{:.2f}".format(3.1415029)
    total = float(total)
    num = int(num)
    min = 0.01
     
    if num < 1:
        return
    if num == 1:
        print "第%d个人拿到红包数:%.2f" % (num,total)
        return
    i = 1
    totalMoney = total
    while(i < num):
        max = totalMoney - min*(num- i)
        k = int((num-i)/2)
        if num -i <= 2:
            k = num -i
        max = max/k
        monney = random.randint(int(min*100), int(max*100))
        monney = float(monney)/100
        totalMoney = totalMoney - monney
        print "第%d个人拿到红包为:%.2f, 余额:%.2f"%(i,monney,totalMoney)
        i += 1
 
    print "第%d个人拿到红包为:%.2f, 余额:%.2f"%(i,totalMoney,0.00)
 
if __name__ == '__main__':
    min = sys.argv[1]
    max = sys.argv[2]
    total = sys.argv[3]
    num = sys.argv[4]
    randBonus(min, max, total, num)
