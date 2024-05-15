import pytest
from mock_alchemy.mocking import AlchemyMagicMock

import source.bank as bank
from source.models import Accounts, Account, Transactions, Transaction


################
### DATABASE ###
################

def test_connection():
    conn, session = bank.connection()
    assert session is not None
    bank.disconnection(conn, session)


def test_disconnection():
    conn, session = bank.connection()
    bank.disconnection(conn, session)
    assert conn.closed, "The connection should be closed"


####################
### END DATABASE ###
####################


#################
### FUNCTIONS ###
#################

def test_create_account():
    conn, session = bank.connection()
    nb_accounts_before = Accounts(session).count()
    bank.disconnection(conn, session)

    session = AlchemyMagicMock()
    assert bank.create_account(session, "10000"), "§101 create_account() failed"

    conn, session = bank.connection()
    nb_accounts_after = Accounts(session).count()
    bank.disconnection(conn, session)
    assert nb_accounts_before == nb_accounts_after, "§102 create_account() failed"


def test_deposit():
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    session = AlchemyMagicMock()
    assert bank.deposit(session, "1", "50", "deposit"), "§201 deposit() failed"

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§202 deposit() failed"


@pytest.mark.skip(reason="not developped")
def test_withdraw():
    pass


@pytest.mark.skip(reason="not developped")
def test_transfer():
    pass


@pytest.mark.skip(reason="not developped")
def test_get_balance():
    pass

#####################
### END FUNCTIONS ###
#####################