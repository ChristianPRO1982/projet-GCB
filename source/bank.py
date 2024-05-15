import pytest
from sqlalchemy import create_engine

from source.models import Account, Transaction


################
### DATABASE ###
################

def connection():
    db_path = 'sqlite:///source/gcb.db'
    engine = create_engine(db_path)
    return engine.connect()


def disconnection(connection):
    connection.close()

####################
### END DATABASE ###
####################


#################
### FUNCTIONS ###
#################

def create_account(conn):
    account = Account(account_id="1", balance="10000")
    conn.add(account)
    conn.commit()


def deposit(conn):
    pass


def withdraw(conn):
    pass


def transfer(conn):
    pass


def get_balance(conn):
    pass

#####################
### END FUNCTIONS ###
#####################