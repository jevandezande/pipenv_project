from pytest import mark

from pipenv_project.pipenv_project import fib


def test_fib():
    assert fib(10) == 55


@mark.xfail
def test_fib_real():
    assert fib(12.3)
