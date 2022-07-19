def fibonacci(n):
    n1=0
    n2=1
    print("Fibonacci series:",end="")
    if n<0:
        print("give a positive number")
    elif n==0 or n==1:
        print(n1,end=" ")
    else:
        print(n1,end=" ")
        print(n2,end=" ")
    
        for i in range(2,n):
        
            sum=n1+n2
            
            n1=n2
            n2=sum
            print(sum,end=" ")
    
        


fibonacci(10)
