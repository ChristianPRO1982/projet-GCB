import pytest
from mock_alchemy.mocking import AlchemyMagicMock
from unittest.mock import patch

import source.bank as bank
from source.models import Accounts, Account, Transactions, Transaction


################
### DEPOSITS ###
################

def test_deposit_ok():
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    with patch('source.models.Accounts.account_exist', return_value=True) as mock_f1 :
        session = AlchemyMagicMock()
        assert bank.deposit(session, "1", "50", "deposit") == 0, "§2.1 deposit() failed"
        mock_f1.assert_called_once_with("1")

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§2.2 deposit() failed"


def test_deposit_ko_Account_doesn_t_exist():
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    with patch('source.models.Accounts.account_exist', return_value=False) as mock_f1 :
        session = AlchemyMagicMock()
        assert bank.deposit(session, "1", "50", "deposit") == 2, "§3.1 deposit() failed"
        mock_f1.assert_called_once_with("1")

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§3.2 deposit() failed"


def test_deposit_ko_Account_doesn_t_exist():
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    with patch('source.models.Accounts.account_exist', return_value=False) as mock_f1 :
        session = AlchemyMagicMock()
        assert bank.deposit(session, "1", "50", "deposit") == 2, "§3.1 deposit() failed"
        mock_f1.assert_called_once_with("1")

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§3.2 deposit() failed"

####################
### END DEPOSITS ###
####################