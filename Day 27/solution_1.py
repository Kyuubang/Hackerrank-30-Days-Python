def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
import random

class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        # complete this function
        return list()

class TestDataUniqueValues(object):

    arr1 = []
    for i in range(10):
        var = random.randint(0,20)
        arr1.append(var)

    @staticmethod
    def get_array():
        # complete this function
        data1 = TestDataUniqueValues.arr1
        return data1


    @staticmethod
    def get_expected_result():
        # complete this function
        min1 = TestDataUniqueValues.get_array()
        return minimum_index(min1)

class TestDataExactlyTwoDifferentMinimums(object):
    arr2 = []
    for i in range(10):
        var2 = random.randint(0,20)
        arr2.append(var2)
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



def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
