import pytest

import source.bank as bank


################
### DATABASE ###
################

@pytest.mark.database
def test_connection():
    conn, session = bank.connection()
    assert session is not None
    bank.disconnection(conn, session)


@pytest.mark.database
def test_disconnection():
    conn, session = bank.connection()
    bank.disconnection(conn, session)
    assert conn.closed, "The connection should be closed"