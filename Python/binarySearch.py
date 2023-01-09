import time
def time_measure(func):
    def wrapper(x,y,z,w):
        start=time.time()
        func(x,y,z,w)
        end=time.time()
        return (end-start)
    return wrapper
#@time_measure
def inBuiltMethod(x,target):
    if target in x:
        return x.index[target]
    else:
        return -1
#@time_measure
def naiveSearch(x,target,z=None,w=None):
    for i in range(len(x)):
        if x[i]==target:
            return i
    return -1
#@time_measure
def binarySearch(x,target,low=None,high=None):
    if low==None:
        low=0
    if high==None:
        high=len(x)-1
    if high<low:
        return -1
    midpoint=(high+low)//2
    if x[midpoint] == target:
        return midpoint
    elif x[midpoint]<target:
        return binarySearch(x,target,midpoint+1,high)
    elif x[midpoint]>target:
        return binarySearch(x,target,low,midpoint-1)
arr=[i for i in range(1000000) if i%2==0]

start=time.time()
binarySearch(arr,102,None,None)
end=time.time()
print(end-start)

start=time.time()
naiveSearch(arr,102,None,None)
end=time.time()
print(end-start)