import pytest
from mock_alchemy.mocking import AlchemyMagicMock
from unittest.mock import patch

import source.bank as bank
from source.models import Transactions


#################
### TRANSFERT ###
#################

@pytest.mark.parametrize(['account_id_withdraw', 'amount', 'Accounts_change_balance', 'error'],
                         [
                             ('5', '10000', True, 0),
                             ('5', '50000', True, 0),
                             ('0', '10000', True, 0),
                             ('0', '5000000', True, 0),
                             ('1', '5000000', True, 0),
                             ('5', '0', True, 2),
                             ('5', '-1', True, 3),
                             ('5', '-0', True, 3),
                             ('5', '-12.34', True, 3),
                             ('5', '12.34', True, 3),
                             ('5', '12.0', True, 3),
                             ('5', '12.00', True, 3),
                             ('5', '12.', True, 3),
                             ('5', '12€', True, 4),
                             ('5', '12 €', True, 4),
                             ('5', '12.34 €', True, 4),
                             ('5', '$12.34', True, 4),
                             ('5', '$ 12.34', True, 4),
                             ('5', '$12', True, 4),
                             ('5', 'plein de tune', True, 4),
                             ('5', '50001', True, 0),
                             ('5', '100000000000', True, 0),
                             ('5', '10000', False, 5),
                         ])
def test_deposit(account_id_withdraw, amount, Accounts_change_balance, error):
    conn, session = bank.connection()
    nb_transactions_before = Transactions(session).count()
    bank.disconnection(conn, session)

    with patch('source.models.Accounts.get_balance') as mock_get_balance,\
         patch('source.models.Accounts.change_balance') as mock_change_balance:
        mock_get_balance.side_effect = [50000]
        mock_change_balance.side_effect = [Accounts_change_balance]
        session = AlchemyMagicMock()
        assert Transactions.create_deposit(session, account_id_withdraw, amount) == error, "§5.1.1 deposit() failed"

    conn, session = bank.connection()
    nb_transactions_after = Transactions(session).count()
    bank.disconnection(conn, session)
    assert nb_transactions_before == nb_transactions_after, "§5.1.2 deposit() failed"