import unittest

import vector as v

class TestEqOverload(unittest.TestCase):
    """Tests for implementing the __eq__ method per exercise 13.4.2."""

    def test_simple_equal(self):
        """Does it return True when two simple vectors are the same?"""
        vector1 = v.Vector((1, 1))
        vector2 = v.Vector((1, 1))
        self.assertEqual(vector1, vector2)
        self.assertTrue(vector1 == vector2)

    def test_unequal_both(self):
        """Does it return False when both x values and y values differ?"""
        vector1 = v.Vector((1, 1))
        vector2 = v.Vector((2, 3))
        self.assertNotEqual(vector1, vector2)
        self.assertFalse(vector1 == vector2)

    def test_unequal_x(self):
        """Does it return False when x values differ and y values are same?"""
        vector1 = v.Vector((1, 2))
        vector2 = v.Vector((3, 2))
        self.assertNotEqual(vector1, vector2)
        self.assertFalse(vector1 == vector2)

    def test_unequal_y(self):
        """Does it return False when x values same, y vals different?"""
        vector1 = v.Vector((1, 1))
        vector2 = v.Vector((1, 3))
        self.assertNotEqual(vector1, vector2)
        self.assertFalse(vector1 == vector2)
           
if __name__ == '__main__':
    unittest.main()
