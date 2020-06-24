"""
Python has built-in assert statement to use assertion condition in the program. 
assert statement has a condition or expression which is supposed to be always true.
Syntax for using Assert in Pyhton:
    assert <condition>
    assert <condition>,<error message>
    
Run this test:
    pytest Chapter-2-writing-test-code/2_asserting_test.py
"""

def test_assert_ok():
    speed = 60
    assert speed < 75
    
def test_assert_not_ok():
    budget = 150
    assert budget != 1000
    assert not budget == 1000  # using not (negation) is expecting condition to false
    
def test_assert_with_message():
    actual_holiday = 'Bandung'
    expected_holiday = 'Bali'
    assert actual_holiday == expected_holiday, f"We expect {actual_holiday} to be {expected_holiday}"
    

import pytest

@pytest.mark.xfail
def test_what_if_the_test_expected_tobe_failure():
    assert 100000 == 1000000000