# Enter your code here. Read input from STDIN. Print output to STDOUT

int_test = int(input())

for i in range(int_test):
    test = input()
    odd = []
    even = []
    for x in range(len(test)):
        if x % 2  == 0 :
            even.append(test[x])
        else :
            odd.append(test[x])
    print("".join(even), "".join(odd))
