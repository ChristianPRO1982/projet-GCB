import os

from models import Accounts, Account, Transactions, Transaction
import bank as bank


####################################################################################################

os.system('clear')
print('DEBUT DU SCRIPT')
conn, session = bank.connection()

####################################################################################################

print("Nombre de comptes", Accounts(session).count())

if not bank.create_account(session, "0"): print("PAS DE COMPTE CREE")
if not bank.create_account(session, "0"): print("PAS DE COMPTE CREE")
if not bank.create_account(session, "10000"): print("PAS DE COMPTE CREE")
if not bank.create_account(session, "5000"): print("PAS DE COMPTE CREE")

print("Nombre de comptes", Accounts(session).count())

####################################################################################################

print("Nombre de transactions", Transactions(session).count())

result = Transactions(session).create_transaction("3", "4", "5000", "transfer")
if result > 0: print(f"PAS DE TRANSACTION CREEE, result:{result}")

print("Nombre de transactions", Transactions(session).count())

####################################################################################################

bank.disconnection(conn, session)
print('FIN DU SCRIPT')
print()