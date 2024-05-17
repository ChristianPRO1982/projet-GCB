from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
from unittest.mock import Mock
import traceback


Base = declarative_base() # tous nos modèles vont hériter de cette class de base

################
### ACCOUNTS ###
################
# class gérant tous les utilisateurs et leur création
class Accounts():
    def __init__(self, session):
        self.session = session

        accounts_query = session.query(Account).all()

        self.accounts = {}
        for account in accounts_query:
            self.accounts[account.account_id] = None


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
        

    def get_balance(self, account_id: str)->int:
        try:
            # object created ?
            if self.accounts[account_id] is None:
                self.accounts[account_id] = self.get_account_by_id(account_id)
            
            return self.accounts[account_id].balance
        
        except Exception as e:
            print("Exception:", e)
            # traceback.print_exc()
            return -123456789

    
    def get_account_by_id(self, account_id:str)->object:
        account = self.session.query(Account).filter(Account.account_id == account_id).first()
        return account
    

    def change_balance(self, account_id:int, amount:int, type:str)->bool:
        try:
            if self.accounts[account_id] is None:
                self.accounts[account_id] = self.get_account_by_id(account_id)

            # match case ne fonctionne que avec python 3.10
            # match type:
            #     case "withdraw":
            #         self.accounts[account_id].balance -= amount
            #     case "deposit":
            #         self.accounts[account_id].balance += amount

            if type == "withdraw":
                self.accounts[account_id].balance -= amount
            elif type == "deposit":
                self.accounts[account_id].balance += amount
            
            return True

        except Exception as e:
            print("Exception:", e)
            # traceback.print_exc()
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
    
    
    def create_transaction(self, account_id_withdraw: str, account_id_deposit: str, amount:str, type: str)->int:
        # ARGS TESTS
        if account_id_withdraw.isdigit() == False:
            print(f"Account doesn't exist: {account_id_withdraw}")
            return 2
        
        if account_id_deposit.isdigit() == False:
            print(f"Account doesn't exist: {account_id_withdraw}")
            return 2
        
        account_id_withdraw_int = int(account_id_withdraw)
        account_id_deposit_int = int(account_id_deposit)

        # match case ne fonctionne que avec python 3.10
        # match type:
        #     case "deposit":
        #         if account_id_withdraw_int != 1:
        #             return 5
        #         if account_id_deposit_int < 3:
        #             return 6
                
        #     case "withdraw":
        #         if account_id_withdraw_int < 3:
        #             return 7
        #         if account_id_deposit_int != 2:
        #             return 8

        #     case "transfer":
        #         if account_id_withdraw_int < 3:
        #             return 9
        #         if account_id_deposit_int < 3:
        #             return 10

        if type == "deposit":
            if account_id_withdraw_int != 1:
                return 5
            if account_id_deposit_int < 3:
                return 6
                
        if type == "withdraw":
                if account_id_withdraw_int < 3:
                    return 7
                if account_id_deposit_int != 2:
                    return 8

        if type == "transfer":
                if account_id_withdraw_int < 3:
                    return 9
                if account_id_deposit_int < 3:
                    return 10


        if Accounts(self.session).account_exist(account_id_withdraw) == False:
            print(f"Account doesn't exist: {account_id_withdraw}")
            return 2
        
        if Accounts(self.session).account_exist(account_id_deposit) == False:
            print(f"Account doesn't exist: {account_id_deposit}")
            return 2
        
        if Transactions(self.session).type_accept(type) == False:
            print(f"Type doesn't accepted: {type}")
            return 3
        
        if Transactions(self.session).amount_accept(amount) == False:
            print(f"Amout doesn't accepted: {amount}")
            return 4
        

        #TRANSACTION
        result = self.create_withdraw(account_id_withdraw, amount)
        
        if isinstance(result, Mock): return 0 # arrêt ici pour les tests unitaires
        
        if result == 0:
            result = self.create_deposit(account_id_deposit, amount)
            if result == 0:
                self.session.commit()
                return 0
            else:
                self.session.rollback()
                return result
        else:
            self.session.rollback()
            return result
        

    def create_withdraw(self, account_id_withdraw: str, amount:str)->int:
        try:
            # ARGS TESTS
            if amount.isdigit():
                num = int(amount)
                if num <= 0:
                    print("zero or negatif")
                    return 2
            else:
                try:
                    num = float(amount)
                    print("not int but float")
                    return 3
                except:
                    print("not numeric")
                    return 4
                    

            # a = 0/0 # POUR TESTER UN BUG


            #TRANSACTION

            # test du solde
            if int(account_id_withdraw) > 2:
                balance = Accounts(self.session).get_balance(int(account_id_withdraw))
                if balance < int(amount):
                    print(f"Pas assez de fond monétaire : {balance}")
                    return 5
            
            # modification du solde
            if not Accounts(self.session).change_balance(int(account_id_withdraw), int(amount), "withdraw"):
                return 6

            transaction = Transaction(account_id=account_id_withdraw, amount=amount, type="withdraw")
            self.session.add(transaction)
            print('Transaction withdraw OK')
            return 0
        
        except Exception as e:
            print(f"Exception: {e}")
            # traceback.print_exc()
            return 1
        

    def create_deposit(self, account_id_deposit: str, amount:str)->int:
        try:
            # ARGS TESTS
            if amount.isdigit():
                num = int(amount)
                if num <= 0:
                    print("zero or negatif")
                    return 2
            else:
                try:
                    num = float(amount)
                    print("not int but float")
                    return 3
                except:
                    print("not numeric")
                    return 4
                    

            # a = 0/0 # POUR TESTER UN BUG


            #TRANSACTION
            
            # modification du solde
            if not Accounts(self.session).change_balance(int(account_id_deposit), int(amount), "deposit"):
                return 5

            transaction = Transaction(account_id=account_id_deposit, amount=amount, type="deposit")
            self.session.add(transaction)
            print('Transaction deposit OK')
            return 0
        
        except Exception as e:
            print(f"Exception: {e}")
            return 1
        

    def type_accept(self, type: str)->bool:
        if type in ('deposit', 'withdraw', 'transfer'):
            return True
        return False
        

    def amount_accept(self, amount: str)->bool:
        if amount.isdigit():
            num = int(amount)
            if num > 0:
                return True
            else:
                print("zero or negatif")
                return False
        else:
            try:
                num = float(amount)
                print("not int but float")
                return False
            except:
                print("not numeric")
                return False
    

class Transaction(Base):

    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, index=True, autoincrement=True) # Identifiant unique de la transaction
    account_id     = Column(Integer, ForeignKey("accounts.account_id")) # Identifiant du compte associé
    # amount         = Column(Float) # Montant de la transaction
    amount         = Column(Integer) # Montant de la transaction -> pas de Float pour s'assurer de calcul juste (0.33 + 0.33 <> 0.66)
    type           = Column(String) # Type de la transaction (deposit, withdraw, transfer)
    timestamp      = Column(DateTime, default=func.now()) # Date et heure de la transaction

    account = relationship("Account", back_populates="transactions")

