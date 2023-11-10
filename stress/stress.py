import unittest


def binarySearch(arr, target):
    if type(target) != int:
        return -1
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        num = arr[mid]

        if num == target:
            return mid
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
class TestBinarySearch(unittest.TestCase):
    def testCase1(self):
        arr = [1, 2, 3, 4, 5]
        target = 300000000000000000000000000000
        result = binarySearch(arr, target)
        self.assertEqual(-1, result)

    def testCase2(self):
        import random
        arr = [random.randint(0, 100000000000000000000000000000) for _ in range(10000000)]
        arr.sort()
        target = random.randint(0, 100000000000000000000000000000)
        result = binarySearch(arr, target)        
        try:
            ans = arr.index(target)
        except ValueError:
            ans = -1
        self.assertEqual(ans, result)
    
    def testCase3(self):
        arr = [50, 100]
        target = "hello"
        result = binarySearch(arr, target)
        self.assertEqual(-1, result)
    
    def testCase4(self):
        arr = [10,100]
        target = None
        result = binarySearch(arr, target)
        self.assertEqual(-1, result)
    def testCase5(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        result = binarySearch(arr, target)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()