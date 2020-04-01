# Enter your code here. Read input from STDIN. Print output to STDOUT
List = []
tester = []
nums = int(input())
for i in range(nums):
    var = list(map(str, input().rstrip().split()))
    lib = tuple(var)
    List.append(lib)
for test in range(nums):
    test = input()
    tester.append(test)
dictionary = dict(List)

for item in tester:
    key = dictionary.get(item)
    if key :
        print(f'{item}={key}')
    else:
        print(f"Not found")
