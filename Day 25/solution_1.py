# Enter your code here. Read input from STDIN. Print output to STDOUT
List = []
params = int(input())
for i in range(params):
    x = int(input())
    List.append(x)

def isPrime(n):

    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
    
for i in (List):
    x = isPrime(i)
    if x:
        print("Prime")
    else :
        print("Not prime")
