import os

import source.bank as bank
from source.models import Accounts, Account, Transactions, Transaction


####################################################################################################

os.system('clear')
print('DEBUT DU SCRIPT')
conn, session = bank.connection()

####################################################################################################

print("Nombre de comptes", Accounts(session).count())

if not bank.create_account(session, "20000"): print("PAS DE COMPTE CREE")
if not bank.create_account(session, "20000"): print("PAS DE COMPTE CREE")
if not bank.create_account(session, "20000"): print("PAS DE COMPTE CREE")

print("Nombre de comptes", Accounts(session).count())

####################################################################################################

print("Nombre de transactions", Transactions(session).count())

if not bank.deposit(session, "120", "50", "coco"): print("PAS DE COMPTE CREE")

print("Nombre de transactions", Transactions(session).count())

####################################################################################################

bank.disconnection(conn, session)
print('FIN DU SCRIPT')
print()