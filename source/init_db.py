# sources :
# https://www.youtube.com/watch?v=g0-7TrVCNtg

from sqlalchemy import create_engine
import os

from models import Base


db_path = 'sqlite:///source/gcb.db'

engine = create_engine(db_path)

os.system('clear')
print("--------------------------------------------------")
try:
    
    conn = engine.connect()
    print("BDD 'gcb.db' créée avec succès !")

    Base.metadata.drop_all(bind=conn)
    Base.metadata.create_all(bind=conn)
    print('Les tables ont été créées !')

except Exception as ex:

    print(ex)

print("--------------------------------------------------")