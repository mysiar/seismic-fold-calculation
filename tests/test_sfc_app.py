import unittest
from bin.sfc_app import _create_db_engine
from sqlalchemy.engine.base import Engine


class SfcAppTestCase(unittest.TestCase):
    def test__create_db_engine(self):
        with self.assertRaises(Exception):
            _create_db_engine("othersql:///tests/data/fold.other", False)

        engine = _create_db_engine("postgresql:///tests/data/fold.other", False)
        self.assertIsInstance(engine, Engine)

        engine = _create_db_engine("sqlite:///tests/data/fold.other", False)
        self.assertIsInstance(engine, Engine)


if __name__ == '__main__':
    unittest.main()
