import pytest
from mock_alchemy.mocking import AlchemyMagicMock
from unittest.mock import patch

import source.bank as bank
from source.models import Accounts, Account, Transactions, Transaction


################
### WITHDRAW ###
################

@pytest.mark.skip(reason="not developped")
def test_withdraw():
    pass

####################
### END WITHDRAW ###
####################