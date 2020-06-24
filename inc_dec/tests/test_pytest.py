import pytest

from inc_dec import increment, decrement   # The code to test


def test_increment():
    assert increment(3) == 4


def test_decrement():
    assert decrement(3) == 2
