# Library-DatabasePostgreSQL-Python

### Created a library to facilitate the sending of any number of fields to the main functions of the SQL database
<br/>

### Library created in Python and can used in any project to acess a database PostgreSQL

<br/>

**In this project is using:** <br/>
- functional paradigm
- dependency injection concept (code clean)
- using PostgreSQL library of Python (install and import psycopg2)
- main SQL database access functions
<br/>

### Configuration data for creating the database connection:

` databaseConfig = {'host': 'localhost', 'database': 'agenda', 'user': 'postgres', 'password': 'admin'} `

### Options for the data used:

1-Create new Table <br/>
2-Add data <br/>
3-Delete data <br/>
4-Delete Table <br/>
5-Update data <br/>
6-Searching all data <br/>
7-Searching by Column <br/>


### Example data:

```
data = {
    'option': 2,
    'tableName': 'Data',
    'fields': ['name', 'email', 'telefone', 'endereco'],
    'data': ['david', 'david@teste.com', '23455', 'street 234'],
    'removeById': 1,
    "updateById": 1,
    "searchByColumn": {"column": "andress", "value": "street 456"}
}
```

### Main:
```
connection = database.createDatabase(databaseConfig)
database.startAction(connection,**data)
database.stopConnection(connection)
```
