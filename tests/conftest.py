import pytest

from source.bank import create_account


@pytest.fixture
def create_account_factory():
    def create_account(account_id, balance):
        return create_account(account_id=account_id, balance=balance)
    return create_account