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

    with patch('source.models.Accounts.account_exist') as mock_account_exist:
        mock_account_exist.side_effect = [True, True]
        session = AlchemyMagicMock()
        assert Transactions.create_transaction(session, "1", "11", "50", "deposit") == 0, "§3.1.1 deposit() failed"

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§3.1.2 deposit() failed"


def test_deposit_ko_account_withdraw_doesn_t_exist():
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    with patch('source.models.Accounts.account_exist') as mock_account_exist :
        mock_account_exist.side_effect = [False, True]
        session = AlchemyMagicMock()
        assert Transactions.create_transaction(session, "1", "11", "50", "deposit") == 2, "§3.2.1 deposit() failed"

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§3.2.2 deposit() failed"


def test_deposit_ko_account_deposit_doesn_t_exist():
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    with patch('source.models.Accounts.account_exist') as mock_account_exist :
        mock_account_exist.side_effect = [True, False]
        session = AlchemyMagicMock()
        assert Transactions.create_transaction(session, "1", "11", "50", "deposit") == 2, "§3.2.1 deposit() failed"

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§3.2.2 deposit() failed"


def test_deposit_ko_type_doesn_t_exist():
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    with patch('source.models.Accounts.account_exist') as mock_account_exist :
        mock_account_exist.side_effect = [True, True]
        session = AlchemyMagicMock()
        assert Transactions.create_transaction(session, "1", "11", "50", "dépo de flouze") == 3, "§3.3.1 deposit() failed"

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§3.3.2 deposit() failed"


@pytest.mark.parametrize('amount', [('not numeric'), ('-1'), ('0'), ('12.23')])
def test_deposit_ko_not_numeric(amount):
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    with patch('source.models.Accounts.account_exist') as mock_account_exist :
        mock_account_exist.side_effect = [True, True]
        session = AlchemyMagicMock()
        assert Transactions.create_transaction(session, "1", "11", amount, "deposit") == 4, "§3.4.1 deposit() failed"

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§3.4.2 deposit() failed"


@pytest.mark.parametrize(['account_id_withdraw', 'account_id_deposit', 'type', 'error'],
                         [
                             ('0', '1', 'deposit', 5),
                             ('2', '1', 'deposit', 5),
                             ('3', '1', 'deposit', 5),
                             ('3', '3', 'deposit', 5),
                             ('1', '0', 'deposit', 6),
                             ('1', '1', 'deposit', 6),
                             ('1', '2', 'deposit', 6),
                             ('0', '2', 'withdraw', 7),
                             ('1', '2', 'withdraw', 7),
                             ('2', '2', 'withdraw', 7),
                             ('10', '0', 'withdraw', 8),
                             ('10', '1', 'withdraw', 8),
                             ('10', '3', 'withdraw', 8),
                             ('10', '11', 'withdraw', 8),
                             ('0', '11', 'transfer', 9),
                             ('1', '11', 'transfer', 9),
                             ('2', '11', 'transfer', 9),
                             ('10', '0', 'transfer', 10),
                             ('10', '1', 'transfer', 10),
                             ('10', '2', 'transfer', 10),
                         ])
def test_deposit_ko_account_error_withdraw_deposit_tranfert(account_id_withdraw, account_id_deposit, type, error):
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    session = AlchemyMagicMock()
    assert Transactions.create_transaction(session, account_id_withdraw, account_id_deposit, "50", type) == error, f"§3.5.{error} deposit() failed"

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§3.5.2 deposit() failed"