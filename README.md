# SGE_BLOC2
# Actividad 5 PYTHON + POSTGRESQL
Guía la configuración de un entorno de desarrollo con Docker, PyCharm y PostgreSQL:
En esta ocación he usado un Ubuntu 20.20 para realizar los siguientes pasos:
Descargaremos Docker desde su página oficial:

![image](https://github.com/user-attachments/assets/734634e7-3f77-4dd4-89ad-bb05a68cab20)

Al instalar el docker me ha aparecido el siguiente error:
![alt text](img/image.png)

Para solucionarlo he accedido a esta página y seguí todos los pasos (https://learn.microsoft.com/es-es/windows/wsl/install).

Una vez tengamos Docker instalado y funcionado, procedemos a instalar PyCharm para Python.
![alt text](img/image-1.png)

Después de instalar PyCharm, comprobaremos que tengamos la versión 3.10. En caso contario tenemos que cambiarla desde la configuración.
![img.png](img/img.png)

Instalaremos el pluggin de Docker, que nos permitirá conectarnos a Docker desde PyCharm y gestionar los contenedores.
![image](https://github.com/user-attachments/assets/1a4bccac-2f06-46e6-bc07-7451d4e2c7f3)

Agreagremos el archivo "docker-compose.yml" y lo configuramos con la siguiente información:
- db: Un contenedor que ejecuta PostgreSQL con un usuario, una contraseña y una base de datos preconfigurados.
- pgAdmin: Una interfaz web para gestionar PostgreSQL, accesible desde el navegador en el puerto 80.

![img_1.png](img/img_1.png)

Desde PyCharm, ejecutaremos el siguiente comando "sudo docker-compose up -d
"en el archivo "docker-compose.yml", teniendo siempre abierto el Docker Desktop :
![alt text](img/image-9.png)
![img_3.png](img/img_3.png)
Después, accedemos a http://localhost:8080 en el navegador y nos registramos con el usuario y la contraseña por defecto puesto en el archivo docker "docker-compose.yml", nos dejará ingresar a pgAdmin 4.
![img_4.png](img/img_4.png)

Creamos un servidor de base de datos del bloque 2
![image](https://github.com/user-attachments/assets/3962075c-99b9-49f1-81cd-cfad964a1fe4)

En "Connection", ingresaremos los datos del container_name, user y password.
![image](https://github.com/user-attachments/assets/a9330aab-ef11-40ba-af9a-6b5bd0f830fe)

Creamos la carpeta bloc2_Brithany en PyCharm. Posterior, en este directorio, crearemos otra carpeta llamada "postgresql_python". Dentro crearemos los siguientes archivos:

### **connect.py:**
![img_6.png](img/img_6.png)


Este archivo establecerá la conexión con la base de datos y poder realizar las operaciones CRUD (Create, Read, Update y Delete) en una tabla de PostgreSQL.
Establece la conexión con PostgreSQL:
python
import psycopg2
conn = psycopg2.connect(dbname='the_bear', user='admin', password='admin', host='localhost', port=5432)

Los datos los he dejado por defecto:
- **Base de datos**: the_bear
- **Usuario**: admin
- **Contraseña**: admin
- **Host**: localhost
- **Puerto**: 5432

Luego, Instalamos las dependencias necesarias:
bash pip install psycopg2 pandas
 en PyCharm es una de las librerías para conectar Python con PostgreSQL, y "pandas" nos permite trabajar con datos en formato de tabla. Además, descargamos el archivo de clientes.csv y lo añadimos en una carpeta con el nombre "send_data_to_db" que estará dentro de la carpeta nuestra carpeta del inicio.
![img_7.png](img/img_7.png)
Verificamos en connect.py:
![img_8.png](img/img_8.png)
En "send_data_to_db" creamos los archivos:

### **create_table_to_db.py:**
![img_9.png](img/img_9.png)

Crea una tabla en la base de datos basada en el archivo ".csv".

### **csv_to_dict.py:**
![image](https://github.com/user-attachments/assets/05362e47-38b4-4b28-86e0-86e6a6715db4)


 Convierte el archivo ".csv" en un diccionario con claves y valores.

### **dict_to_db.py**
![image](https://github.com/user-attachments/assets/dad241b0-7611-42aa-9eed-f9c0291912e8)

Inserta datos en la base de datos a partir del diccionario.

### **create_register.py**
![alt text](img/image-4.png)

Permite insertar nuevos registros en la base de datos.

### **main.py**
![image](https://github.com/user-attachments/assets/5710dbbe-f56f-4579-a287-22562a08ceb2)

Archivo principal para ejecutar la aplicación.

Comprobación de los datos en pgAdmin
Refrescamos la tabla de clientes en **pgAdmin4** refrescar la tabla de clientes y ejecutarla para que se muestren los datos introducidos.
![img_10.png](img/img_10.png)
Finalmente, debemos agregar los últimos códigos CRUD:

### **read_registre.py**

![alt text](img/image-5.png)
Aquí estamos imprimiendo todos los registros de la tabla Clientes. Cada fila de la tabla está representada como una tupla dentro de la lista. Cada tupla contiene las columnas de la tabla (nombre, dirección, teléfono, correo, fecha de cumpleaños).
![img_11.png](img/img_11.png)

![img_12.png](img/img_12.png)
Aquí estamos extrayendo el registro del cliente con id_cliente = 5 de la lista de resultados.
Recupera y muestra todos los registros de la tabla "clientes".

![img_13.png](img/img_13.png)
Aquí hemos extraído el teléfono del cliente con id_cliente = 5

![img_14.png](img/img_14.png)
Comprobaciones de:
Les dades de l’Andreu, El correu de l’Andreu, Les dades de la Vivian, La direcció de la Vivian ,Les dades de l’Albert ,La data de cumpleanys de l’Albert

![img_15.png](img/img_15.png)
Se muestra la información de cada cliente, como su nombre, dirección, teléfono, correo y fecha de nacimiento.
### **update_registre.py**

![img_18.png](img/img_18.png)
![img_19.png](img/img_19.png)

Modifica datos de un cliente en la base de datos en este caso fue el número de teléfono de los tres.

### **delete_registre.py**

![img_21.png](img/img_21.png)
![img_22.png](img/img_22.png)
Elimina un registro de los tres que pusismos en delete_registre si lo buscamos podremos ver que ya no existen esos tres:

