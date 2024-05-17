import pytest
from mock_alchemy.mocking import AlchemyMagicMock
from unittest.mock import patch

import source.bank as bank
from source.models import Accounts, Account, Transactions, Transaction


###############
### BALANCE ###
###############

@pytest.mark.parametrize(['account_id_withdraw', 'amount', 'Accounts_change_balance', 'error'],
                         [
                             ('5', '10000', True, 0),
                             ('5', '10000', True, 0),
                         ])
def test_get_balance(account_id_withdraw, amount, Accounts_change_balance, error):
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    with patch('source.models.Accounts.get_balance') as mock_get_balance:
        mock_get_balance.side_effect = [50000]
        session = AlchemyMagicMock()
        assert Transactions.create_deposit(session, account_id_withdraw, amount) == error, "§6.1.1 deposit() failed"

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§6.1.2 deposit() failed"