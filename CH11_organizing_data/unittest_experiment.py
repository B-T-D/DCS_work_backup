import unittest

def x_squared(x):
    return x * x

class TestXSquared(unittest.TestCase):

    def test_common_case(self):
        self.assertEqual(x_squared(2), 4)

if __name__ == '__main__':
    unittest.main()
