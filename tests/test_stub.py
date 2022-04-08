from pipenv_project.pipenv_project import fib


def test_fib():
    assert fib(10) == 55
