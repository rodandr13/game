from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

# pprint(game_stamps)


def check_arguments(game_stamps, offset):
    if not isinstance(game_stamps, list) or not game_stamps:
        raise ValueError(
            "game_stamps должен быть списком и содержать временные отметки"
        )
    if not isinstance(offset, int):
        raise TypeError("offset должен быть int")
    elif (offset < 0) or (offset > TIMESTAMPS_COUNT * OFFSET_MAX_STEP):
        raise ValueError(f"offset должен больше 0 и меньше {TIMESTAMPS_COUNT * OFFSET_MAX_STEP}")


def get_score(game_stamps, offset):
    check_arguments(game_stamps, offset)
    low = 0
    high = len(game_stamps) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = game_stamps[mid]
        if not isinstance(guess["offset"], int):
            raise TypeError("guess[\"offset\"] должен быть int")
        try:
            if guess["offset"] == offset:
                home = guess["score"]["home"]
                away = guess["score"]["away"]
                return home, away
            elif guess["offset"] > offset:
                high = mid - 1
            else:
                low = mid + 1
        except KeyError as error:
            raise KeyError("game_stamps имеет неверную структуру", error)

    return None


# print(get_score(test, 1))

