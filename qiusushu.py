#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def getSushu(n):
    count=0
    l=[i%2==1 for i in range(0,n+1)]
    l[2]=True
    for i in range(3,int(n**0.5)+1,2):
        if l[i]:
            for j in range(i+i,n+1,i):
                l[j]=False
    for i in range(2,n+1):
        if l[i]:
            count += 1
            print i,
    print '\n','%d内共有%d个素数'%(n,count)

def test():
    print 'hello world'

if __name__=='__main__':
    n=int(sys.argv[1])
    getSushu(n)
