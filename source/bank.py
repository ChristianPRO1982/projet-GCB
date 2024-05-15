from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from source.models import Accounts, Account, Transaction


################
### DATABASE ###
################

def connection():
    db_path = 'sqlite:///source/gcb.db'
    engine = create_engine(db_path)
    conn = engine.connect()
    Session = sessionmaker(bind=conn)
    return conn, Session()


def disconnection(conn, session):
    session.close()
    conn.close()

####################
### END DATABASE ###
####################


#################
### FUNCTIONS ###
#################

def create_account(session):
    accounts = Accounts(session)
    accounts.create_account(balance="20000")


def deposit(session):
    pass


def withdraw(session):
    pass


def transfer(session):
    pass


def get_balance(session):
    pass

#####################
### END FUNCTIONS ###
#####################