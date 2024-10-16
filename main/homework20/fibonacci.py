import unittest

class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


class TestFibonacci(unittest.TestCase):
    def test_zero_number(self):
        fibonacci = Fibonacci()
        self.assertEqual(fibonacci(0), 0)

    def test_negative_limit(self):
        with self.assertRaises(ValueError):
            Fibonacci()(-1)

    def test_normal_case(self):
        fibonacci = Fibonacci()
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(10), 55)

    def test_large_number(self):
        fibonacci = Fibonacci()
        self.assertEqual(fibonacci(500), 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125)

    def test_float_raise(self):
        with self.assertRaises(ValueError):
            Fibonacci()(1.1)

    def test_type_raise(self):
        with self.assertRaises(ValueError): Fibonacci()('1')
        with self.assertRaises(ValueError): Fibonacci()(None)
        with self.assertRaises(ValueError): Fibonacci()([1, 2, 3])
        with self.assertRaises(ValueError): Fibonacci()((1, 2, 3))
        with self.assertRaises(ValueError): Fibonacci()({1: 2})
        with self.assertRaises(ValueError): Fibonacci()({1, 2, 3, 4})

def main():
    # print(Fibonacci()(0))
    unittest.main()

if __name__ == "__main__":
    main()
