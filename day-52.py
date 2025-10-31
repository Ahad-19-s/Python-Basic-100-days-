def double(x):
    return x*2
print (double(5))

double = lambda x,y:x*y
print(double(5,8))




avg=lambda x,y,z: (x+y+z)/3

print(avg(5,3,4))

def appl(fx,a,b,c):
    return 10+fx(a,b,c)

print(appl(avg,2,3,4))

