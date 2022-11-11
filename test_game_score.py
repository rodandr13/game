import unittest
import random

from game_score import get_score, generate_game, TIMESTAMPS_COUNT, OFFSET_MAX_STEP


class TestGameScore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_game_stamps = [
             {'offset': 0, 'score': {'away': 0, 'home': 0}},
             {'offset': 2, 'score': {'away': 1, 'home': 0}},
             {'offset': 4, 'score': {'away': 2, 'home': 1}},
             {'offset': 7, 'score': {'away': 2, 'home': 1}}
        ]
        cls.invalid_game_stamps = [
             {'offset': 0, 'score': {'away': [], 'home': '0'}},
             {'offset': '2', 'score': {'away': 1, 'home': 0}},
        ]

    def test_valid_arguments(self):
        call = get_score(self.valid_game_stamps, 2)
        result = (0, 1)
        self.assertEqual(call, result)

    def test_invalid_argument_score(self):
        with self.assertRaises(TypeError):
            get_score(self.invalid_game_stamps, 0)

    def test_invalid_argument_type_offset(self):
        with self.assertRaises(TypeError):
            get_score(self.invalid_game_stamps, 2)

    def test_invalid_argument_value_offset(self):
        max_offset = TIMESTAMPS_COUNT * OFFSET_MAX_STEP + 1
        for i in (-1, max_offset):
            with self.subTest(value=i):
                self.assertRaises(
                    ValueError, get_score, self.valid_game_stamps, i
                )

    def test_missing_offset_in_game_stamps(self):
        call = get_score(self.valid_game_stamps, 1)
        self.assertIsNone(
            call,
            "Функция должна возвращать None "
            "при отсутствии временной отсечки offset в game_stamps"
        )


if __name__ == '__main__':
    unittest.main()
