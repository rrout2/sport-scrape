import unittest

from fantasy_football_data import FantasyFootballData

def huh():
    x = 7

class TestFantasyFootballData(unittest.TestCase):
    def test_empty_constructor(self):
        data = FantasyFootballData()
        self.assertNotEqual(data, None)
        self.assertEqual(data.teams, [])
        self.assertEqual(data.matchups, {})

if __name__ == '__main__':
    unittest.main()