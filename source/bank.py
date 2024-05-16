from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    from models import Accounts, Account, Transactions, Transaction
except:
    from source.models import Accounts, Account, Transactions, Transaction


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

def create_account(session, balance: str)->bool:
    accounts = Accounts(session)
    return accounts.create_account(balance=balance)