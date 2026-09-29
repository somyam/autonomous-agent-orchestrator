"""Unit tests for mathematical agent skills."""
import pytest
from src.skills.math_skills import compute_fibonacci

def test_fibonacci_zero_and_negative():
    """Verify that input less than or equal to 0 returns 0."""
    assert compute_fibonacci(0) == 0
    assert compute_fibonacci(-5) == 0

def test_fibonacci_base_cases():
    """Verify standard early sequence values."""
    assert compute_fibonacci(1) == 1
    assert compute_fibonacci(2) == 1

def test_fibonacci_large_value():
    """Verify a deeper sequence number (n=10 should be 55)."""
    assert compute_fibonacci(10) == 55
