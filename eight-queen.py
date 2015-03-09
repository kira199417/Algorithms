def check(queenlist,col):
    next_row=len(queenlist)
    for i in range(next_row):
        if abs(queenlist[i]-col) in (0,next_row-i):
            return False
    return True
def print_out(queenlist):

    for col in queenlist:
        x=0
        while x<8:
            if x==col:
                print 'Q',
            else:
                print '.',
            x+=1
        print '\n'
row=col=count=0
queenlist=[]
while col<8:
    if check(queenlist,col):
        queenlist.append(col)
        col=0
        row+=1
        if len(queenlist) is 8:
            #print queenlist
            print_out(queenlist)
            count+=1
            col=queenlist.pop()+1
            if col is 8:
                col=queenlist.pop()+1
            row-=1
        continue
    else:
        col+=1
    if col is 8:
        col=queenlist.pop()+1
        if col==8 and len(queenlist)!=0:
            col=queenlist.pop()+1
        row-=1
print count
