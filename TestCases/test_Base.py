import pytest

"""Base class for all test_ classes"""
@pytest.mark.usefixtures("driver_setup")
class BaseTest:
    pass