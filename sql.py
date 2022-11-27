def removeCommon(sql):
    size = len(sql)
    sql = sql[0:size-2]    
    sql += ")"
    return sql

def fieldsSQL(tableName, fields):
    sql = 'CREATE TABLE {} (id SERIAL PRIMARY KEY, ' .format(tableName)    
    for c in fields:
        sql += c + " VARCHAR(30), "
    sql = removeCommon(sql)
    return sql

def insertDataSQL(tableName, fields, data):
    sql = "INSERT into " +tableName+ " ("
    for c in fields:
        sql += c+ ", "
    sql = removeCommon(sql)
    sql += " values("
    for d in data:
        sql += "'{}', ".format(d)
    sql = removeCommon(sql)
    return sql
 
def deleteDataSQL(tableName, idToRemove):
    sql = "DELETE FROM {} WHERE id={}".format(tableName, idToRemove)
    return sql

def updateSQL(tableName, fields, data, updateById):
    sql = "UPDATE {} SET ".format(tableName)
    i = 0
    for f in fields:
        sql += "{} = '{}', ".format(f, data[i])
        i += 1
    sql = removeCommon(sql)
    size = len(sql)
    sql = sql[0:size-1]    
    sql += " WHERE id = {}".format(updateById)
    return sql

def searchAllSQL(tableName):
    sql = "SELECT * FROM {}".format(tableName)
    return sql

def searchByColumnSQL(tableName, column, value):
    if type(value) == str:
      sql = "SELECT * FROM {} WHERE {} = '{}'".format(tableName, column, value) 
    else: 
      sql = "SELECT * FROM {} WHERE {} = {}".format(tableName, column, value)
    return sql