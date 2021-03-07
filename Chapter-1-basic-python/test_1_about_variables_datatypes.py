"""
To create a variable in Python, all you need to do is specify the variable name, and then assign a value to it.
<variable name> = <value>
Python uses = to assign values to variables.
"""


def test_assigning_var():
    # String type
    saying = "hello world"
    print(saying)

    # Integer
    age = 17
    print("My age is", age)

    some_long_int = 38563846326424324
    assert isinstance(some_long_int, int)

    # Floating point
    pi = 3.14
    print("Pi is", pi)
    c = 123456789.e1
    assert isinstance(c, float)

    # Boolean
    male = True
    print(male)
    assert isinstance(male, bool)

    # Empty value
    x = None
    print(x)


def test_assign_multiple():
    a, b, c = 1, 2, 3
    print("a:", a)
    print("b:", b)
    print("c:", c)

    d, e = 4, 5, 6      # will throw error to unpack, Note that there must be the same number of arguments on the right and left sides of the = operator:
    print(d, e)


def test_tupple():
    """
    Supports indexing; immutable; hashable if all its members are hashable
    """
    num = (1, 3, 4, 2)
    print(num)

    # using tuple, index start from 0
    print(num[2])
    
    # defined without bracket
    selector = 'id', 3,
    assert isinstance(selector, tuple)
    print(selector)


def test_list():
    """
    Not hashable; mutable.
    """
    basket = ['apple', 'melon', 'durian']

    print(basket[2])          # usage by using index
    basket.append('manggo')   # adding one element at the end
    print(basket)
    assert len(basket) == 4
    basket.remove('melon')
    assert len(basket) == 3
    
    for fruit in basket:
        print("Name:", fruit)


def test_set():
    """
    An unordered collection of unique values. Items must be hashable
    """
    a = {1, 2, 'a'}
    print(a)


def test_dict():
    """
    An unordered collection of unique key-value pairs; keys must be hashable.
    """
    student = {'name': 'Fachrul', 'live': 'Bekasi', 'height': 169}
    # usage
    assert student['name'] is 'Fachrul'
    assert student.get('height') is 169
    student['name'] = 'Mas Fachrul'   # dict is mutable, it can be changed
    assert student['name'] is not 'Fachrul'

    for key in student.keys():
        print("this is the attributes :", key)
    print("=== Info Student ===")
    for key, val in student.items():
        print(f"{key} : {val}")