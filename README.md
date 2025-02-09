# SGE_BLOC2
# Actividad 5 PYTHON + POSTGRESQL
Guía la configuración de un entorno de desarrollo con Docker, PyCharm y PostgreSQL:
En esta ocación he usado un Ubuntu 20.20 para realizar los siguientes pasos:
Descargaremos Docker desde su página oficial:

![image](https://github.com/user-attachments/assets/734634e7-3f77-4dd4-89ad-bb05a68cab20)

Al instalar el docker me ha aparecido el siguiente error:
![alt text](image.png)

Para solucionarlo he accedido a esta página y seguí todos los pasos (https://learn.microsoft.com/es-es/windows/wsl/install).

Una vez tengamos Docker instalado y funcionado, procedemos a instalar PyCharm para Python.
![alt text](image-1.png)

Después de instalar PyCharm, comprobaremos que tengamos la versión 3.10. En caso contario tenemos que cambiarla desde la configuración.
![image](https://github.com/user-attachments/assets/0bfcec37-f4cb-49b2-b5d8-12cdbc45ab8a)

Instalaremos el pluggin de Docker, que nos permitirá conectarnos a Docker desde PyCharm y gestionar los contenedores.
![image](https://github.com/user-attachments/assets/1a4bccac-2f06-46e6-bc07-7451d4e2c7f3)

Agreagremos el archivo "docker-compose.yml" y lo configuramos con la siguiente información:
- db: Un contenedor que ejecuta PostgreSQL con un usuario, una contraseña y una base de datos preconfigurados.
- pgAdmin: Una interfaz web para gestionar PostgreSQL, accesible desde el navegador en el puerto 80.

![3](https://github.com/user-attachments/assets/578f07d1-cafa-4f48-a94f-e512670b7b76)

Desde PyCharm, ejecutaremos el siguiente comando "sudo docker-compose up -d
"en el archivo "docker-compose.yml", teniendo siempre abierto el Docker Desktop :
![1](https://github.com/user-attachments/assets/f14eb01c-8277-49af-af65-74e99a6b7ebc)

Después, accedemos a http://localhost:80 en el navegador y nos registramos con el usuario y la contraseña por defecto puesto en el archivo docker "docker-compose.yml", nos dejará ingresar a pgAdmin 4.
![image](https://github.com/user-attachments/assets/2a0716a7-3082-4fe8-b896-828ccb30551c)

Creamos un servidor de base de datos del bloque 2
![image](https://github.com/user-attachments/assets/3962075c-99b9-49f1-81cd-cfad964a1fe4)

En "Connection", ingresaremos los datos del container_name, user y password.
![image](https://github.com/user-attachments/assets/a9330aab-ef11-40ba-af9a-6b5bd0f830fe)

Creamos la carpeta `bloc2_NOMALUMNX` en PyCharm. Posterior, en este directorio, crearemos otra carpeta llamada "postgresql_python". Dentro crearemos los siguientes archivos:

### **connect.py**
![image](https://github.com/user-attachments/assets/8384095b-4b2c-496e-bdca-489abf41b1b6)

Este archivo establecerá la conexión con la base de datos y poder realizar las operaciones CRUD (Create, Read, Update y Delete) en una tabla de PostgreSQL.

Los datos los he dejado por defecto:
- **Base de datos**: the_bear
- **Usuario**: admin
- **Contraseña**: admin
- **Host**: localhost
- **Puerto**: 5432

Luego, en PyCharm, instalamos los plugins. "psycopg2" es una de las librerías para conectar Python con PostgreSQL, y "pandas" nos permite trabajar con datos en formato de tabla. Además, descargamos el archivo de clientes.csv y lo añadimos en una carpeta con el nombre "send_data_to_db" que estará dentro de la carpeta nuestra carpeta del inicio.

En "send_data_to_db" creamos los archivos:

### **create_table_to_db.py**
![image](https://github.com/user-attachments/assets/ebae9996-4abf-494d-90e7-3bb6d4a324ec)

Que sirve para leer el archivo ".csv" para determinar los nombres y tipos de columnas y luego crear una tabla en la base de datos PostgreSQL con esos campos.

### **csv_to_dict.py**
![image](https://github.com/user-attachments/assets/05362e47-38b4-4b28-86e0-86e6a6715db4)

Transformará el archivo `.csv` en una lista de diccionarios. Cada fila será un diccionario donde las claves son los nombres de las columnas y los valores los datos correspondientes.

### **dict_to_db.py**
![image](https://github.com/user-attachments/assets/dad241b0-7611-42aa-9eed-f9c0291912e8)

### **create_register.py**
![image](https://github.com/user-attachments/assets/4135f0b1-f0d4-464d-bcc8-547f7cdde8e7)

### **main.py**
![image](https://github.com/user-attachments/assets/5710dbbe-f56f-4579-a287-22562a08ceb2)

Para comprobar que los datos se han añadido, debemos ir a **pgAdmin4**, refrescar la tabla de clientes y ejecutarla para que se muestren los datos introducidos.
![image](https://github.com/user-attachments/assets/23373626-0c1e-457e-9d6a-55800ff1e907)

Finalmente, debemos agregar los últimos códigos:

### **read_registre.py**

![read_registre.py](https://github.com/user-attachments/assets/9dd46f56-ea2d-47d5-8f7f-7b266f8362f3)

conecta a la base de datos y recupera todos los registros de la tabla clientes, mostrando los datos en la terminal.

### **update_registre.py**

![update_registre.py](https://github.com/user-attachments/assets/38be6ed6-03c9-4d0d-a623-c215b8ff60bc)

permite actualizar los datos de un cliente en la base de datos. Busca un registro por su ID y modifica los campos especificados.

### **delete_registre.py**

![delete_registre.py](https://github.com/user-attachments/assets/9d241fc2-731c-495e-b3b0-0c42d04d9fcb)

Un registro específico de la tabla clientes según el ID proporcionado, asegurando que los datos se borren de la base de datos.

