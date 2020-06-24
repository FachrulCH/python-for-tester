import some_module
from some_package import addition
from some_package.multiply import multiply


# A module is a single Python file that can be imported. Using a module looks like this:
def test_using_module():
    some_module.greeting()


def test_using_package():
    result = multiply(3,3)                  # see line 3 when importing full path, function can directly use
    result_add = addition.add(1000, 300)    # see line 2, when importing only file name, we need to using module name to invoke function
    assert result == 9
    assert result_add == 1300