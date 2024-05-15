import pytest
from mock_alchemy.mocking import AlchemyMagicMock
from unittest.mock import patch

import source.bank as bank
from source.models import Accounts, Transactions


################
### ACCOUNTS ###
################

def test_create_account():
    conn, session = bank.connection()
    nb_accounts_before = Accounts(session).count()
    bank.disconnection(conn, session)

    session = AlchemyMagicMock()
    assert bank.create_account(session, "10000"), "§1.1 create_account() failed"

    conn, session = bank.connection()
    nb_accounts_after = Accounts(session).count()
    bank.disconnection(conn, session)
    assert nb_accounts_before == nb_accounts_after, "§1.2 create_account() failed"

####################
### END ACCOUNTS ###
####################