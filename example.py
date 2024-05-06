"""
Example script for a mock DB
"""

from library.read import ReadDB
from library.create import CreateDB
from library.write import WriteDB

print("dynamicDB Example V1")

# Example
FILE_NAME = "./posts.dn"
FUNCTION = "WRITE"
schema = 'data\nfields id,username,postCount fields\n1,Joe,4000\nend_data'

# Functions
CreateDB(FILE_NAME, schema)
WriteDB(FILE_NAME, [[1,'Ski',4]])
print(ReadDB(FILE_NAME))