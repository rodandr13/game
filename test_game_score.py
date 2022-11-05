import unittest
import random

from game_score import get_score, generate_game, TIMESTAMPS_COUNT, OFFSET_MAX_STEP


class TestGetScore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.game_stamps = generate_game()
        cls.offset = random.randint(0, TIMESTAMPS_COUNT * OFFSET_MAX_STEP)
        cls.get_score = get_score(TestGetScore.game_stamps, TestGetScore.offset)

    def test_invalid_argument_type_offset(self):
        self.assertRaises()
        print(self.get_score)


if __name__ == '__main__':
    unittest.main()
