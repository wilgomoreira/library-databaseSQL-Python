import psycopg2, sql, os

def createDatabase(databaseConfig):
    os.system('cls')
    connection = connectionDatabase(**databaseConfig)
    return connection

def startAction(connection, option, tableName, fields, data, removeById, updateById, searchByColumn):
    switchDatabase(option, connection, tableName, fields, data, removeById, updateById, searchByColumn)  

def stopConnection(connection):
    connection.close()
  
def switchDatabase(option, connection, tableName, fields, data, removeById, updateById, searchByColumn):
    if option == 1:
      #create Table
      fieldsSQL = sql.fieldsSQL(tableName, fields)
      createTable(connection, fieldsSQL, tableName)
    elif option == 2:
      #insert Data
      dataSQL = sql.insertDataSQL(tableName, fields, data)
      insertInTable(connection, dataSQL, tableName)
    elif option == 3:
      #delete Data
      removeDataSQL = sql.deleteDataSQL(tableName, removeById)
      deleteInTable(connection,removeDataSQL, tableName)
    elif option == 4:
      #delete Table
      removeTable(connection, tableName)
    elif option == 5:
      #update Data
      updateDataSQL = sql.updateSQL(tableName, fields, data, updateById)
      updateInTable(connection, updateDataSQL, tableName)
    elif option == 6:
      #search all Data
      searchSQL = sql.searchAllSQL(tableName)
      searchInTable(connection, searchSQL, tableName,fields)
    elif option == 7:
      #serch by column
      searchColumnSQL = sql.searchByColumnSQL(tableName, **searchByColumn)
      searchInTableByColumn(connection, searchColumnSQL, tableName, fields, **searchByColumn)

def connectionDatabase(host, database, user, password):
    try: 
      connection = psycopg2.connect(host=host, database=database, user=user, password=password)
      print('Connection with Database '+database+' done!!')
      return connection
    except:
      print('Error in connection with database '+database+' !!')

def createTable(connection, sql, tableName):
    try:
      #Remove Table before Create
      cursor = connection.cursor()
      sqlremove = 'DROP TABLE IF EXISTS ' +tableName
      cursor.execute(sqlremove)   
      connection.commit()
      #create Table
      cursor = connection.cursor()
      cursor.execute(sql)
      connection.commit()
      print("Table "+tableName+" created!!!")
    except:
      print('Error in create Table: ' +tableName)

def insertInTable(connection, sql, tableName):
    try:
      cursor = connection.cursor()
      cursor.execute(sql)
      connection.commit()
      print('Data insert in Table '+tableName+'!!')
    except:
      print('Error in insert data in Table '+tableName+'!!')

def deleteInTable(connection, sql, tableName):
    try:
      cursor = connection.cursor()
      cursor.execute(sql)
      connection.commit()
      print('Remove data in Table '+tableName+'!!')
    except:
      print('Error in remove data in Table '+tableName+'!!')

def removeTable(connection, tableName):
    try:
      #Remove Table before Create
      cursor = connection.cursor()
      sqlremove = 'DROP TABLE IF EXISTS ' +tableName
      cursor.execute(sqlremove)   
      connection.commit()
      print("Table "+tableName+" removed!")
    except:
      print('Error in remove Table: ' +tableName)

def updateInTable(connection, sql, tableName):
    try:
      cursor = connection.cursor()
      cursor.execute(sql)
      connection.commit()
      print('Update data in Table '+tableName+'!!')
    except:
      print('Error Update data in Table '+tableName+'!!')

def searchInTable(connection, sql, tableName, fields):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print('Searching all data in Table '+tableName+'!!')
    text = ' Id'
    for f in fields:
      text += ' | ' +f
    print(text)
    if len(result) == 0:
      print("Table empty")
      return
    for res in result:
      print(res)

def searchInTableByColumn(connection, sql, tableName, fields, column, value):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print('Searching the value '+value+' in column '+column+' in Table '+tableName+'!!')
    text = ' Id'
    for f in fields:
      text += ' | ' +f
    print(text)
    if len(result) == 0:
      print("Nothing found!!")
      return
    for res in result:
      print(res)


    
