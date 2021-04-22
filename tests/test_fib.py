#  Project yo is developed by Fahad Ahammed on 4/23/21, 12:02 AM.
#
#  Last modified at 4/23/21, 12:02 AM.
#
#  Github: fahadahammed
#  Email: obak.krondon@gmail.com
#
#  Copyright (c) 2021. All rights reserved.

import unittest

from yo import fib


class TestFib(unittest.TestCase):
    def test_int(self):
        data = 5
        result = fib(data)
        self.assertEqual(result, [0, 1, 1, 2, 3])

    def test_list_int(self):
        data = [1, 2, 3]
        with self.assertRaises(TypeError):
            result = fib(data)

    def test_negative_int(self):
        data = -90
        result = fib(data)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()