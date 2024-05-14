from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base() # tous nos modèles vont hériter de cette class de base

class Account(Base):

    __tablename__ = 'accounts'

    account_id = Column(Integer, primary_key=True, index=True) # Identifiant unique du compte
    balance    = Column(Float) # Solde du compte

    transactions = relationship("Transaction", back_populates="account")


class Transaction(Base):

    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, index=True) # Identifiant unique de la transaction
    account_id     = Column(Integer, ForeignKey("accounts.account_id")) # Identifiant du compte associé
    amount         = Column(Float) # Montant de la transaction
    # amount         = Column(Integer) # Montant de la transaction -> pas de Float pour s'assurer de calcul juste (0.33 + 0.33 <> 0.66)
    type           = Column(String) # Type de la transaction (deposit, withdraw, transfer)
    timestamp      = Column(DateTime) # Date et heure de la transaction

    account = relationship("Account", back_populates="transactions")
    