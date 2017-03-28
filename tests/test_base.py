import os
import unittest
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class TestBase(unittest.TestCase):

    def test_command(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        logger.info(f"base directory: {base_dir}")
        self.assertEqual('asdf', 'asdf')


if __name__ == '__main__':
    logger.info('calling unittest.main()')
    unittest.main()
    logger.info('end unittest.main()')
