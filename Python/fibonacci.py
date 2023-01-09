temp=0;
x=0
y=1
z=0
fibonacci_list=[];
print(1)
while z<20:
    temp=y
    
    y=x+y
    x=temp
    
    temp=x
    fibonacci_list.append(y)
    z+=1
print(fibonacci_list);

