import math, time, unittest


def all_distinct(a, b):
    result = set()
    for i in range(a, b + 1):
        for j in range(a, b + 1):
            result.add(pow(i, j))

    return len(result)


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(all_distinct(2, 5), 15)


start_time = time.time()
print(all_distinct(2, 100))
print("--- %s seconds ---" % (time.time() - start_time))
