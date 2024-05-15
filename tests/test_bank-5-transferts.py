import pytest
from mock_alchemy.mocking import AlchemyMagicMock
from unittest.mock import patch

import source.bank as bank
from source.models import Accounts, Account, Transactions, Transaction


#################
### TRANSFERT ###
#################

@pytest.mark.skip(reason="not developped")
def test_transfer():
    pass

#####################
### END TRANSFERT ###
#####################