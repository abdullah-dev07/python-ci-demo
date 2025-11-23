# tests/test_app.py
from app import calculate_sum, welcome_message

# --- Passing Tests ---

def test_welcome_message():
    """Tests the basic greeting message."""
    assert "Hello from the CI Pipeline!" in welcome_message()

def test_calculate_sum_success():
    """Tests the sum function with a correct assertion."""
    assert calculate_sum(2, 3) == 5

# --- Failing Test (For Demo) ---

def test_calculate_sum_failure_demo():
    """This test is designed to FAIL to show an Unstable build in Jenkins."""
    # 2 + 2 equals 4, so asserting it equals 5 will cause a failure.
    assert calculate_sum(2, 2) == 5