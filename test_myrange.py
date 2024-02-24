#test_myrange.py

import unittest
from myrange import *

class MyRangeTests(unittest.TestCase):
    def setUp(self):
        self._r = get_range(5)
        
    def test_can_generate_range_with_given_parameters(self):
        self.assertEqual(list(get_range(0, 5, 1)), [0, 1, 2, 3, 4])

    def test_can_generate_range_with_only_stop(self):
        self.assertEqual(list(self._r), list(get_range(0, 5, 1)))

    def test_can_return_correct_parameters(self):
        self.assertEqual(self._r.start(), 0)
        self.assertEqual(self._r.stop(), 5)
        self.assertEqual(self._r.step(), 1)

    def test_can_be_iterated_in_reverse(self):
        self.assertEqual(list(get_range(3, 0, -1)), [3, 2, 1])

    def test_raises_error_if_iterated_past_stop(self):
        with self.assertRaises(StopIteration):
            i = iter(self._r)
            for x in range(6):
                next(i)

    def test_parameters_must_be_integers(self):
        with self.assertRaises(TypeError):
            r = get_range(8.5)

    def test_obj_is_represented_correctly(self):
        self.assertEqual(self._r.__repr__(), 'MyRange(0, 5, 1)')

    def test_myrange_object_is_sizable(self):
        self.assertEqual(len(MyRange(5, 8, 2)), 2)

    def test_myrange_object_is_hashable_can_be_added_to_set(self):
        s = {1, 2, 3, MyRange(4, 8, 1)}

    def test_myranges_with_equal_parameters_are_equivalent(self):
        self.assertTrue(self._r.__eq__(get_range(5)))

    def test_myrange_cannot_be_compared_to_other_objects(self):
        self.assertEqual(self._r.__eq__(range(5)), NotImplemented)

    def test_myrange_can_be_indexed(self):
        self.assertEqual(self._r[0], 0)
        self.assertEqual(self._r[1], 1)

    def test_out_of_bounds_index_raises_error(self):
        with self.assertRaises(IndexError):
            self._r[5]
        with self.assertRaises(IndexError):
            self._r[-1]

    def test_myrange_can_be_sliced(self):
        self.assertEqual(self._r[:-1], get_range(4))
        self.assertEqual(self._r[1:4], get_range(1, 4))
        self.assertEqual(self._r[::2], get_range(0, 5, 2))
        self.assertEqual(self._r[::-1], get_range(4, -1, -1))

    def test_non_integer_index_raises_error(self):
        with self.assertRaises(TypeError):
            self._r[1.6]

if __name__ == '__main__':
    unittest.main()
