import libv
print("Found lib", libv.__path__)
print(dir(libv))

from libv.utils.main import foo

def test_foo():
    assert foo(2, 3) == 5


def test_foo_new():
    assert foo(5, 7) == 12