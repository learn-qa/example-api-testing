import pytest

from src.test.step_defs.UsersHelper import UsersHelper


@pytest.fixture
def application():
    helper = UsersHelper()
    return helper
