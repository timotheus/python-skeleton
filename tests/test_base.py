import os
import unittest


class TestBase(unittest.TestCase):

    def test_command(self):
        # base_dir = os.path.dirname(os.path.abspath(__file__))
        self.assertEqual('asdf', 'asdf')


if __name__ == '__main__':
    unittest.main()