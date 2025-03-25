import connect

def update_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update_1 = '''
    UPDATE clientes
    SET teléfono_cliente = '1111111'
    WHERE nombre_cliente = 'Juan Manuel'
    '''
    sql_update_2 = '''
    UPDATE clientes
    SET teléfono_cliente = '2222222'
    WHERE nombre_cliente = 'Alba'
    '''
    sql_update_3 = '''
    UPDATE clientes
    SET teléfono_cliente = '3333333'
    WHERE nombre_cliente = 'Mireia'
    '''

    cursor.execute(sql_update_1)
    cursor.execute(sql_update_2)
    cursor.execute(sql_update_3)

    conn.commit()

    cursor.close()
    conn.close()

    return {"Update successfully"}