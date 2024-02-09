# Tests are defined here
from ukp_project_template import BaseClass

def test_template():
    assert True

def test_base_class():
    bc1 = BaseClass(name="test1")
    bc2 = BaseClass(name="test2")

    assert str(bc1) == "test1"
    assert repr(bc1) == "test1"
    assert bc1 != bc2