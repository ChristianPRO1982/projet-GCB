import pytest

import source.bank as bank


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

    assert session is not None
    
    bank.disconnection(conn, session)
    assert True


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