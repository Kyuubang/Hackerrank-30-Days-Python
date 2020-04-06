#Write your code here
class Calculator(object):
    def power(self, n, p):
        if (n>0) and (p>0):
            return(n**p)
        elif (n<0) or (p<0):
            raise Exception("n and p should be non-negative")


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
