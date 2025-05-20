from sqlalchemy import create_engine,text

from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:root1234@127.0.0.1:3306', echo=True)

# creamos la base de datos si no existe
with engine.connect() as conn:
    conn.execute(text('CREATE DATABASE IF NOT EXISTS data'))
    print('Base de datos creada')


# Ahora conectamos a la base de datos recien creada
engine = create_engine('mysql+mysqlconnector://root:root1234@127.0.0.1:3306/data', echo=True)
Session_maker = sessionmaker(bind= engine)



