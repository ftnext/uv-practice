from mylib import hello


def test_always_true():
    assert 1 == 1


def test_hello():
    assert hello() == "Hello from mylib!"
