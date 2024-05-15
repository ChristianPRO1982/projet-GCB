import pytest

import source.bank as bank


################
### DATABASE ###
################

def test_connection():
    conn = bank.connection()
    assert conn is not None
    bank.disconnection(conn)


def test_disconnection():
    conn = bank.connection()
    bank.disconnection(conn)
    assert conn.closed

####################
### END DATABASE ###
####################


#################
### FUNCTIONS ###
#################

def test_create_account():
    assert False


@pytest.mark.skip
def test_deposit():
    pass


@pytest.mark.skip
def test_withdraw():
    pass


@pytest.mark.skip
def test_transfer():
    pass


@pytest.mark.skip
def test_get_balance():
    pass

#####################
### END FUNCTIONS ###
#####################