from db import engine, Session_maker
from models import Usuarios, Base


# Crear tablas
Base.metadata.create_all(engine)

# Crear sesion
session = Session_maker()

# insertar datos de prueba
usuario1 = Usuarios('Michaela Jenkins', 'michaela@gmail.es', 'mk40ella')
usuario2 = Usuarios('Sarah Thompson', 'sarahTh@gmail.co', 'tHsarah90')
usuario3 = Usuarios('Jordan Lara', 'jordanLa@gmail.com', 'jordan7890')
usuario4 = Usuarios('James Milton', 'miltonJ4@hotmail.es', 'Jmil9078')

session.add_all([usuario1, usuario2, usuario3, usuario4])
session.commit()
session.close()
print('Usuarios insertados')





