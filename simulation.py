import os

import source.bank as bank


os.system('clear')
print('DEBUT DU SCRIPT')
conn, session = bank.connection()

bank.create_account(session)

bank.disconnection(conn, session)

print('FIN DU SCRIPT')
print()