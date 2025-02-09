# SGE_BLOC2
# Actividad 5 PYTHON + POSTGRESQL
Guía la configuración de un entorno de desarrollo con Docker, PyCharm y PostgreSQL:
En esta ocación he usado un Ubuntu 20.20 para realizar los siguientes pasos:
Podemos descargar Docker desde su página oficial. Nos será útil, ya que nos permite crear y gestionar contenedores, que son entornos aislados donde podemos ejecutar aplicaciones sin preocuparnos por las diferencias entre sistemas operativos.
![image](https://github.com/user-attachments/assets/734634e7-3f77-4dd4-89ad-bb05a68cab20)

Una vez que Docker está instalado y funcionando, procedemos a instalar PyCharm, un entorno de desarrollo integrado (IDE) para Python.
![image](https://github.com/user-attachments/assets/ed72d987-5dd8-49db-b556-6cff646cd1cd)

Después de instalar PyCharm, lo primero que debemos comprobar es que tengamos la versión 13.10. En caso de que tengamos otra versión, podemos cambiarla desde la configuración.
![image](https://github.com/user-attachments/assets/0bfcec37-f4cb-49b2-b5d8-12cdbc45ab8a)

Luego, desde allí mismo nos instalamos el plugin de Docker, que nos permitirá conectarnos a Docker desde PyCharm y gestionar contenedores.
![image](https://github.com/user-attachments/assets/1a4bccac-2f06-46e6-bc07-7451d4e2c7f3)

El archivo `docker-compose.yml` contiene lo siguiente:
![3](https://github.com/user-attachments/assets/578f07d1-cafa-4f48-a94f-e512670b7b76)
- **db**: Un contenedor que ejecuta PostgreSQL con un usuario, una contraseña y una base de datos preconfigurados.
- **pgAdmin**: Una interfaz web para gestionar PostgreSQL, accesible desde el navegador en el puerto 80.

En PyCharm, ejecutamos el archivo `docker-compose.yml`, asegurándonos de que Docker Desktop está activo. Para ello, utilizamos el siguiente comando en la terminal:
![1](https://github.com/user-attachments/assets/f14eb01c-8277-49af-af65-74e99a6b7ebc)

Luego, en la terminal, accedemos a http://localhost:80 en el navegador y nos registramos con el usuario y la contraseña por defecto, que están en el archivo `docker-compose.yml`, para ingresar a pgAdmin 4.
![image](https://github.com/user-attachments/assets/2a0716a7-3082-4fe8-b896-828ccb30551c)

Allí creamos un servicio de base de datos con un nombre personalizado.
![image](https://github.com/user-attachments/assets/3962075c-99b9-49f1-81cd-cfad964a1fe4)

En la sección **Connection**, ingresamos los siguientes datos:
![image](https://github.com/user-attachments/assets/a9330aab-ef11-40ba-af9a-6b5bd0f830fe)
Con esto, el contenedor se llama `db_erp` y utiliza el usuario `admin` y la contraseña `admin` para entrar en el servidor.

Creamos la carpeta `bloc2_NOMALUMNX` en PyCharm Community. Dentro de esta carpeta, creamos otra carpeta llamada `postgresql_python`. Dentro de esta carpeta, creamos los siguientes archivos:

### **connect.py**
![image](https://github.com/user-attachments/assets/8384095b-4b2c-496e-bdca-489abf41b1b6)

Este código sirve para establecer la conexión con la base de datos y poder realizar las operaciones CRUD (Create, Read, Update y Delete) en una tabla de PostgreSQL.

Los datos que se utilizan en la conexión:
- **Base de datos**: the_bear
- **Usuario**: admin
- **Contraseña**: admin
- **Host**: localhost
- **Puerto**: 5432

Estos datos se extraen del archivo `docker-compose.yml` creado en la configuración de Docker. Además, imprime el objeto de conexión indicando que está abierta (`closed: 0`), luego la cierra con `connect.close()` y vuelve a imprimir el objeto, ahora indicando que está cerrada (`closed: 1`).

Luego, en PyCharm, instalamos los plugins. `psycopg2` es una librería para conectar Python con PostgreSQL, y `pandas` nos permite trabajar con datos en formato de tabla. Además, descargamos el archivo de clientes en formato `.csv` y lo añadimos en una carpeta con el nombre `send_data_to_db` que estará dentro de la carpeta `bloc2`.

Dentro de `send_data_to_db` creamos los siguientes archivos:

### **create_table_to_db.py**
![image](https://github.com/user-attachments/assets/ebae9996-4abf-494d-90e7-3bb6d4a324ec)

Se encargará de leer el archivo `.csv` para determinar los nombres y tipos de columnas y luego crear una tabla en la base de datos PostgreSQL con esos campos.

