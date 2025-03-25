import psycopg2

def read_reg():
    conn = psycopg2.connect(
        database="the_bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM Clientes;")

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results  # ⬅️ Ahora devuelve los datos correctamente