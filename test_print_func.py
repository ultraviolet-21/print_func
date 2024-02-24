#Testing the recreated print function

import unittest
from print_func import *

class PrintTests(unittest.TestCase):
    def test_empty_statement_returns_empty_string(self):
        self.assertEqual(p(), '')
        
    def test_one_string_can_be_returned(self):
        self.assertEqual(p('Chance'), 'Chance')
        
    def test_non_str_types_converted_to_str(self):
        self.assertEqual(p(1), '1')
        self.assertEqual(p([1, 2, 3, 4, 5]), '[1, 2, 3, 4, 5]')
        self.assertEqual(p(range(0, 5)), 'range(0, 5)')
        
    def test_multiple_args_can_be_passed_using_default_sep_and_end(self):
        self.assertEqual(p('Boo', 'is', 'happy', 'today'), 'Boo is happy today')
        
    def test_multiple_args_can_be_passed_with_custom_sep_and_end(self):
        self.assertEqual(p(*['Life', 'is', 'soup', 'I', 'am', 'fork'], sep = ',', end = '!'),
                         'Life,is,soup,I,am,fork!')
        
    def test_custom_sep_has_no_effect_with_only_one_arg(self):
        self.assertEqual(p('2', sep = '#'), '2')



if __name__ == '__main__':
    unittest.main()
