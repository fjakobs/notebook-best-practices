import pytest

@pytest.mark.skip(reason="This is a boring test")
def test_skip():
    assert True
