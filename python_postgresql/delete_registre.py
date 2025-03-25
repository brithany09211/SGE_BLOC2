import connect
def delete_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_delete_1 = '''
    DELETE FROM clientes
    WHERE nombre_cliente = 'Juan Manuel'
    '''

    sql_delete_2 = '''
    DELETE FROM clientes
    WHERE nombre_cliente = 'Alba'
    '''

    sql_delete_3 = '''
    DELETE FROM clientes
    WHERE nombre_cliente = 'Mireia'
    '''

    cursor.execute(sql_delete_1)
    cursor.execute(sql_delete_2)
    cursor.execute(sql_delete_3)

    conn.commit()

    conn.close()
    cursor.close()
