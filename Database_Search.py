import pymysql

keyword='input you want to search the keyword'
cnx = pymysql.connect(user='Database_Username', password='Database_Password', host='Database_host',port=3306,database='database_name')

cursor = cnx.cursor()

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    
    cursor.execute("DESCRIBE " + table_name)
    fields = cursor.fetchall()
    
    select_stmt = "SELECT "
    for field in fields:
        select_stmt += field[0] + ", "
    select_stmt = select_stmt[:-2] + " FROM " + table_name
    
    query = select_stmt + " WHERE "
    for field in fields:
        query += field[0] + " LIKE '%"+keyword+"%' OR "
    query = query[:-4]

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

cursor.close()
cnx.close()
