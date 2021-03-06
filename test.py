import unittest
from mymodule import add_integers

class TesMyModule(unittest.TestCase):

    def test_add_integeers_with_integers(self):
        self.assertEqual(add_integers(1, 2), 3)
    def test_add_integers_negative(self):
        n1 = -2
        n2 = 0
        expected_value = n1 +n2
        self.assertEqual(
            add_integers(n1, n2),
            expected_value
        )
    def test_add_integers_error_if_not_int(self):
        n1 = 3/8
        n2 = 27/5
        self.assertRaises(TypeError(
            add_integers(n1, n2),
            expected_value
        ))

        def test_assert_int_int_raises_no_error(self):
            for n in range(-100, 101):
                self.assertTrue(assert_int(1))


    def test_assert_int_non_int_raises_typerror(self):
        pass

if __name__ == '__main__':
    unittest.main()
