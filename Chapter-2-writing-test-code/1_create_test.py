"""
    1. Naming file
        File name should has word "test" at the begining (prefix) or at the end (surfix)
    2. Method naming
        A test method should defined using prefix "test_" so the pytest would recognize this method as a test to run
        Name using underscore by convention for more readable method name
    3. Running test
        Open the terminal and type "pytest Chapter-2-writing-test-code/1_create_test.py"
"""


def test_add():
    result = 20 + 30
    assert result == 50


"""
Following test is expected to fail, observe the pytest test result (ouput in terminal)
can you undertand the error report?
"""


def test_add_failed():
    result = 20 + 30
    assert result != 50


def test_assert_failed_will_stop_execution():
    expected_money = 1000
    actual_money = 75
    assert actual_money == expected_money
    print("This statement wont executed :( ")
    assert actual_money > 0


"""
Test can also be grouped inside class, it usefull when you need to sharing context to other similar test
"""


class TestUsingClass:
    OBJECT_TO_TEST = ['apple', 'kiwi', 'durian', 'rambutan']

    def test_first(self):
        assert self.OBJECT_TO_TEST[0] == 'apple'

    def test_durian(self):
        assert self.OBJECT_TO_TEST[2].upper() == 'DURIAN'

    def test_want_more(self):
        assert len(self.OBJECT_TO_TEST) > 10
