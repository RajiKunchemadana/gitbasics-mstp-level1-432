def add(a,b):
        c=a+b
        print(c)
def prime(n):
    f=0
    for i in range(1,n+1):
        if(n%i==0):
            f=f+1
    if(f==2):
         return True
    else:
        return False

        