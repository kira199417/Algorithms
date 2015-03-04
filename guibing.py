def merge(numbers,start,middle,end):
    temp1=numbers[start:middle+1]
    temp2=numbers[middle+1:end]
    temp2.append(numbers[end])
    i=j=0
    k=start
    while i<=len(temp1) and j<=len(temp2):
        if temp2[j]<temp1[i]:
            numbers[k]=temp2[j]
            j+=1
        else:
            numbers[k]=temp1[i]
            i+=1
        k+=1
    if i>len(temp1):
            while j<=len(temp2):
                numbers[k]=temp2[j]
                j+=1
                k+=1
    else:
        while i<len(temp1):
            numbers[k]=temp1[i]
            i+=1
            k+=1
    return numbers
def merge_sort(numbers,start,end):
    if start<end:
        middle=(start+end)/2
        merge_sort(numbers,start,middle)
        merge_sort(numbers,middle+1,end)
        merge(numbers,start,middle,end)
    return numbers
numbers=[23,12,2,4,52,13]
new=merge_sort(numbers,0,len(numbers)-1)
print new
