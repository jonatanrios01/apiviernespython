from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

#conexion a la base de datos 
#nombreBD
dataBaseName="gestionbd"

#usurioBD
userName="root"

#contraseña del Usuario
userPassword=""

#puerto de conexion
conexionPort="3306"

serverConnection="localhost"

#CREANDO LA CONEXION
connetionToDatabase=f"mysql+mysqlconnector://{userName}:{userPassword}@{serverConnection}:{conexionPort}/{dataBaseName}"

engine=create_engine(connectionToDataBase)
sessionLocal=sessionmaker(autocomit=False, autoflush=False, bind=engine)

