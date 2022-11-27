import database

databaseConfig = {'host': 'localhost', 'database': 'agenda', 'user': 'postgres', 'password': 'admin'}
# OPTIONS:
# 1-Create new Table
# 2-Add data
# 3-Delete data
# 4-Delete Table
# 5-Update data
# 6-Searching all data
# 7-Searching by Column
data1 = {
    'option': 2,
    'tableName': 'Data',
    'fields': ['nome', 'email', 'telefone', 'endereco'],
    'data': ['davi', 'davi@teste.com', '23455', 'rua tiradentes'],
    'removeById': 1,
    "updateById": 1,
    "searchByColumn": {"column": "endereco", "value": "rua tiradentes"}
}
data2 = {
    'option': 7,
    'tableName': 'Data',
    'fields': ['nome', 'email', 'telefone', 'endereco'],
    'data': ['marta', 'marta@teste.com', '23455', 'rua tiradentes'],
    'removeById': 1,
    "updateById": 2,
    "searchByColumn": {"column": "email", "value": "marta@teste.com"}
}
data3 = {
    'option': 6,
    'tableName': 'Data',
    'fields': ['nome', 'email', 'telefone', 'endereco'],
    'data': ['wil', 'wil@teste.com', '23455', 'rua tiradentes'],
    'removeById': 1,
    "updateById": 1,
    "searchByColumn": {"column": "email", "value": "davi@teste.com"}
}
connection = database.createDatabase(databaseConfig)
database.startAction(connection,**data1)
database.startAction(connection,**data2)
database.startAction(connection,**data3)
database.stopConnection(connection)








