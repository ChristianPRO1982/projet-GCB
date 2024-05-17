import pytest
from unittest.mock import patch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import source.bank as bank
from source.models import Base, Accounts, Account


# Configuration de la base de données en mémoire pour les tests
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)

# Utilisez la session avec la base de données en mémoire
session = Session()

@pytest.fixture(scope='module', autouse=True)
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


###############
### BALANCE ###
###############

@patch.object(Accounts, 'get_account_by_id')
@pytest.mark.parametrize(['account_id', 'balance'],
                         [
                             (0, 50),
                             (1, 500),
                             (2, 5000),
                             (3, 50000),
                             (10000, 500000),
                         ])
def test_get_balance_ok(mock_get_account_by_id, account_id, balance):
    # Configurez le mock pour retourner un objet Account simulé
    mock_account = Account(account_id=account_id, balance=balance)
    mock_get_account_by_id.return_value = mock_account

    accounts = Accounts(session)

    # Testez la méthode get_balance
    assert accounts.get_balance(account_id, True) == balance, "§6.1.1 deposit() failed"
    mock_get_account_by_id.assert_called_once_with(account_id)


@patch.object(Accounts, 'get_account_by_id')
@pytest.mark.parametrize(['account_id', 'balance'],
                         [
                             (0, 50),
                             (1, 500),
                             (2, 5000),
                             (3, 50000),
                             (10000, 500000),
                         ])
def test_get_balance_ok(mock_get_account_by_id, account_id, balance):
    # Configurez le mock pour retourner un objet Account simulé
    mock_account = Account(account_id=account_id, balance=balance)
    mock_get_account_by_id.return_value = mock_account

    accounts = Accounts(session)

    # Testez la méthode get_balance
    assert accounts.get_balance(account_id, True) == balance, "§6.1.1 deposit() failed"
    mock_get_account_by_id.assert_called_once_with(account_id)


@pytest.mark.parametrize(['account_id', 'balance'],
                         [
                             (0, 50),
                             (1, 500),
                             (2, 5000),
                             (3, 50000),
                             (10000, 500000),
                         ])
def test_get_balance_ko_no_mock(account_id, balance):
    accounts = Accounts(session)
    assert accounts.get_balance(account_id, False) == "-123456789", "§6.2.1 deposit() failed"


@pytest.mark.skip(reason="not developed")
def test_function_not_developed():
    assert True


@pytest.mark.xfail(reason="test with bug")
def test_function_crash():
    assert False