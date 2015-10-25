'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''
import time, math, unittest


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_of_digits(32768), 26)


start_time = time.time()
print(sum_of_digits(int(math.pow(2,1000))))
print("--- %s seconds ---" % (time.time() - start_time))
