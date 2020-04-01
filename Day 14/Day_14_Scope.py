class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        num = self.__elements
        #global List
        List = []
        for _ in range(len(num)):
            for i in range(len(num)):
                dif = num[_] - num[i]
                List.append(abs(dif))
    def maximumDifference(self):
        print(max(list))


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
