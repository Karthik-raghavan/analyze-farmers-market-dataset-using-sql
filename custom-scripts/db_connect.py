class database:
    def connect_to_mysql_db(host, port, database, user,password,query):
        import pandas as pd
        import pymysql

        db = pymysql.connect(host = host,
        port = port,
        database=database,
        user = user,
        password = password)

        cursor = db.cursor()
        cursor.execute(query)

        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]

        data = pd.DataFrame(cursor.fetchall(), columns = field_names)

        return data