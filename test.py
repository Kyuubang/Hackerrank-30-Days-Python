import random
#bay

class TestDataExactlyTwoDifferentMinimums(object):
    arr2 = []
    for i in range(10):
        var2 = random.randint(0,20)
        arr2.append(var2)

    @staticmethod
    def get_array():
        # complete this function
        data2 = TestDataExactlyTwoDifferentMinimums.arr2
        return data2

    @staticmethod
    def get_expected_result():
        # complete this function
        min2 = TestDataExactlyTwoDifferentMinimums.get_array()
        return minimum_index(min2)
