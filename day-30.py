# 7 factoral 
def factorial(n):
    if(n==0 or n==1):
        return 1;
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(4))

f0=0
f1=1
def fibonaci (n):
    if n<=0:
        return []
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    else:
        seq= fibonaci(n-1)
        seq.append(seq[-1] + seq[-2])
        return seq 
    
num=int(input("How may terms ? :"))
print(fibonaci(num))
    