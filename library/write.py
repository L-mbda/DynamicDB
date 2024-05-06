def WriteDB(FILE_NAME, input_data):
    # Define Optional Variables
    # input_data = [['roblox','fortnite',200],['rebex','mrbaest',300]]
    reading_db = open(FILE_NAME, 'r')
    unopen_db = reading_db.readlines()[:-1]
    reading_db.close()
    for data in input_data:
        finalized_input = ','.join(list(map(str, data)))
        unopen_db.append(f'{finalized_input}\n')
    unopen_db.append('end_data')
    writing_db = open(FILE_NAME, 'w')
    writing_db.write(''.join(unopen_db))
    writing_db.close()
    # # return True