import math
import random
import string
import time
import unittest

import typing_game
    
class Play(unittest.TestCase):
    def test_play(self):
        EXPECTED_LPS = 25  # max human LPS is 15ish
        letters = string.ascii_lowercase + string.ascii_uppercase + " "
        line = ''.join(random.choice(letters) for i in range(100))
        def autoplay(idx):
            time.sleep(1/EXPECTED_LPS) 
            return str.encode(line[idx])
        lps = typing_game.play(line, autoplay)
        assert math.isclose(lps, EXPECTED_LPS, rel_tol = 0.1), f"LPS {lps:.2f} is not close to expected {EXPECTED_LPS}"

if __name__ == "__main__":
    unittest.main()
