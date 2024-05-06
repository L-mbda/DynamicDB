def ReadDB(file):
    db = open(file,'r')
    read = db.readlines()
    db.close()
    
    # Flags, Fields, and Data
    FLAG_READING = False
    header_fields = None
    r_data = []
    version = None

    # Reading Logic
    for data in read:
        resulting_data = data.split('\n')[0]
        parsing_equals = [resulting_data.split(' = ')]
        for i in range(len(parsing_equals)):
            if len(parsing_equals[i]) > 1:
                if parsing_equals[i][0] == "dDB_version":
                    version = parsing_equals[i][1].split('"')[1]
            elif parsing_equals[i][0] == 'data':
                FLAG_READING = True
            elif parsing_equals[i][0] == "end_data":
                FLAG_READING = False
            elif FLAG_READING:
                if parsing_equals[i][0].split(" ")[0] == 'fields' and parsing_equals[i][0].split(" ")[-1] == 'fields':
                    header_fields = parsing_equals[i][0].split(" ")[1:-1][0].split(',')
                else:
                    r_data.append(parsing_equals[i][0].split(','))
    return [header_fields, r_data], version