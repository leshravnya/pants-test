import libv
print("Found lib", libv.__path__)
print(dir(libv))

from libv.utils.main import foo

def test_foo():
    assert foo(2, 3) == 5
