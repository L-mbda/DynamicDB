def CreateDB(FILE_NAME, schema):
    created_db = open(FILE_NAME, 'w')
    created_db.write(f'dDB_version = "1.0B"\n{schema}')