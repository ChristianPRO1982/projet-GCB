from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base() # tous nos modèles vont hériter de cette class de base

################
### ACCOUNTS ###
################
# class gérant tous les utilisateurs et leur création
class Accounts():
    def __init__(self, session):
        self.session = session

        accounts_query = session.query(Account).all()

        self.accounts = []
        for account in accounts_query:
            self.accounts.append(account.account_id)


    def count(self):
        return len(self.accounts)
    
    
    def create_account(self, balance: str)->bool:
        try:
            account = Account(balance=balance)

            # a = 0/0 # POUR TESTER UN BUG

            self.session.add(account)
            self.session.commit()
            print('Account created')
            return True
        except Exception as e:
            print(e)
            return False
        

    def account_exist(self, account_id: str)->bool:
        result = self.session.query(Account).filter(Account.account_id == account_id).count()
        if result > 0:
            return True
        else:
            return False


# class gérant gérant qu'un seul utilisateur
class Account(Base):

    __tablename__ = 'accounts'

    account_id = Column(Integer, primary_key=True, index=True, autoincrement=True) # Identifiant unique du compte
    balance    = Column(Float) # Solde du compte

    transactions = relationship("Transaction", back_populates="account")


####################
### TRANSACTIONS ###
####################
class Transactions():
    def __init__(self, session):
        self.session = session

        transaction_query = session.query(Transaction).all()

        self.transactions = []
        for transaction in transaction_query:
            self.transactions.append(transaction.transaction_id)


    def count(self):
        return len(self.transactions)
    
    
    def create_transaction(self, account_id: str, amount:str, type: str)->bool:
        try:
            transaction = Transaction(account_id=account_id, amount=amount, type=type)

            # a = 0/0 # POUR TESTER UN BUG

            self.session.add(transaction)
            self.session.commit()
            print('Transaction OK')
            return True
        except Exception as e:
            print(f"Exception: {e}")
            return False
        

    def type_accept(self, type: str)->bool:
        if type in ('deposit', 'withdraw', 'transfer'):
            return True
        return False
    

class Transaction(Base):

    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, index=True, autoincrement=True) # Identifiant unique de la transaction
    account_id     = Column(Integer, ForeignKey("accounts.account_id")) # Identifiant du compte associé
    # amount         = Column(Float) # Montant de la transaction
    amount         = Column(Integer) # Montant de la transaction -> pas de Float pour s'assurer de calcul juste (0.33 + 0.33 <> 0.66)
    type           = Column(String) # Type de la transaction (deposit, withdraw, transfer)
    timestamp      = Column(DateTime) # Date et heure de la transaction

    account = relationship("Account", back_populates="transactions")
    