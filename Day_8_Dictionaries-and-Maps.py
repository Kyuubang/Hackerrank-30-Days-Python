def counting(n,s):
    List = list(s)
    for i in range(1,n+1):
        if s[i] == "U":
            print("_/")
        else:
            print("_\n"+" "*i,"\\")


counting(5,"DU")
print("_\n"+" "*i,"\\")
