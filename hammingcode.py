def calcRedundantBits(m):
    	for i in range(m):
            if(2**i >= m + i + 1):
                return i
def posRedundantBits(data,r):
    j = 0
    k = 0
    m = len(data)
    res = ''
    data=data[::-1]
    for i in range(1, m+1+r):
        if(i == 2**j):
            res = res + 'x'
            j += 1
        else:
            res = res + data[k]
            k += 1   
    return res[::-1]  
t=[]    
def calcParityBits(arr, r):
    n=len(arr)
    l=[]  
    for i in arr:
        if i == 'x':
            l.append(0)
        else:
            l.append(int(i))    
    arr=l 
    for i in range(r):
        val = 0       
                # 1110
                # 11
        for j in range(1, n + 1):
            
            if(j & (2**i) == (2**i)):
                val = val ^ (arr[-1 * j])
                # -1 * j is given since array is reversed

        t.append(val)

    return arr
    
data='1001101'
r=calcRedundantBits(len(data))
# print(r)
arr=posRedundantBits(data,r)   
ar=list(arr)
# print(ar)
arr=calcParityBits(ar,r)
print(arr)
print(t)
f=''
for i in ar:
    if i == 'x':
        f=f+str(t.pop())
    else:
        f=f+i
print('Final answer',f)          
