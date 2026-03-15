import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📈 Go HIGHER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📉 Go LOWER!")

@pytest.mark.parametrize("guess, secret, expected_outcome, expected_message", [
    (77, 20, "Too High", "📈 Go HIGHER!"),
    (15, 20, "Too Low", "📉 Go LOWER!"),
    (20, 20, "Win", "🎉 Correct!"),
    (99, 100, "Too Low", "📉 Go LOWER!"),
    (100, 99, "Too High", "📈 Go HIGHER!"),
])
def test_check_guess_integer_comparison(guess, secret, expected_outcome, expected_message):
    # Bug was: secret sometimes str, now always int
    outcome, message = check_guess(guess, secret)
    assert outcome == expected_outcome
    assert message == expected_message
