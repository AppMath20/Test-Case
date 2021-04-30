import main
import pytest

"""
Testing module.
"""


@pytest.mark.great
def test_1():
    student = main.return_result('java -jar _Student_code.jar')
    author = main.return_result('java -jar _Author_code.jar')
    assert student == author, "The data doesn't match"


@pytest.mark.great
def test_2():
    assert main.analyze_code() == True, "The for loop is not used or the data output is not organized correctly"


def function_python(num):
    return num


@pytest.mark.randomize(num=int, min_num=2, max_num=100, ncalls=3)
def test_3(num):
    result = list(function_python(num))
    assert (len(result) == num)
