import unittest
from bin.sfc_app import _create_db_engine, timer
from sqlalchemy.engine.base import Engine
import time


class SfcAppTestCase(unittest.TestCase):
    def test__create_db_engine(self):
        with self.assertRaises(Exception):
            _create_db_engine("othersql:///tests/data/fold.other", False)

        engine = _create_db_engine("postgresql:///tests/data/fold.other", False)
        self.assertIsInstance(engine, Engine)

        engine = _create_db_engine("sqlite:///tests/data/fold.other", False)
        self.assertIsInstance(engine, Engine)

    def test_timer(self):
        start = time.time()
        end = time.time() + 62368
        result = timer(start, end)
        self.assertEqual('17:19:28.00', result)


if __name__ == '__main__':
    unittest.main()
