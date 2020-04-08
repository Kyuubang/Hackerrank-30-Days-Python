# Enter your code here. Read input from STDIN. Print output to STDOUT
x = (input().split())
y = (input().split())
year = x.pop()
years = y.pop()
if int(year) > int(years):
    print(10000)
elif int(year) < int(years):
    print(0)
elif year == years:
    hackos = [15,500]
    for i in ((range(2))[::-1]):
        if int(x[i]) > int(y[i]):
            print((int(x[i])-int(y[i]))*(hackos[i]))
            break
        elif int(x[i]) == int(y[i]):
            continue
        else :
            print(0)
            break
