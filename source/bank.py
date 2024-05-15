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


def deposit(session, account_id: str, amount:str, type: str)->int:
    # ARGS TESTS
    if Accounts(session).account_exist(account_id) == False:
        print(f"Account doesn't exist: {account_id}")
        return 2
    
    if Transactions(session).type_accept(type) == False:
        print(f"Type doesn't accepted: {type}")
        return 3
    
    if Transactions(session).amount_accept(amount) == False:
        print(f"Amout doesn't accepted: {amount}")
        return 4
    
    
    transactions = Transactions(session)
    if transactions.create_transaction(account_id=account_id, amount=amount, type=type):
        return 0
    else:
        return 1


def withdraw(session, account_id: str, amount:str, type: str)->int:
    pass


def transfer(session, account_id: str, amount:str, type: str)->int:
    pass


def get_balance(session)->int:
    pass

#####################
### END FUNCTIONS ###
#####################