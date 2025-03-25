import psycopg2

def create_tables():
   conn = psycopg2.connect(
       database="the_bear",
       password="admin",
       user="admin",
       host="localhost",
       port="5432"
   )

   cursor = conn.cursor()

   sql_clients = '''
       CREATE TABLE Clientes (
       Nombre_Cliente VARCHAR(100),
       Dirección_Cliente VARCHAR(200),
       Teléfono_Cliente VARCHAR(100),
       Correo_Electrónico_Cliente VARCHAR(100),
       Fecha_Cumpleaños VARCHAR(50));'''

   cursor.execute(sql_clients)  # ← Todo correctamente alineado

   conn.commit()

   cursor.close()  # ← Primero se cierra el cursor
   conn.close()  # ← Luego se cierra la conexión

   return {"Tables created succesfully"}  # ← Se mantiene el return del profesor

# Llamar a la función para ejecutarla
create_tables()
