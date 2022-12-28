import unittest


class FirstSampleTest(unittest.TestCase):

    # Return true or false.
    def test_StringUpper(self):
        self.assertEqual('foo'.upper(), 'F2OO', 'Something wrong')


if __name__ == '__main__':
    unittest.main()