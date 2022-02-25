import math
import time
import unittest

import typing_game
    
class Play(unittest.TestCase):
    def test_play(self):
        EXPECTED_LPS = 25  # max human LPS is 15ish
        def autoplay(idx):
            time.sleep(1/EXPECTED_LPS) 
            return str.encode(typing_game.LINE[idx])
        lps = typing_game.play(autoplay)
        assert math.isclose(lps, EXPECTED_LPS, rel_tol = 0.1), f"LPS {lps} is not close to expected {EXPECTED_LPS}"

if __name__ == "__main__":
    unittest.main()
