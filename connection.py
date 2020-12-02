import psycopg2

class Connection():

    def get_connection(self):
        connection = psycopg2.connect(user="postgres",
                                      password="8pcapdoe6gdd",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="N3_crud_api")
        print("Database Connected")
        return connection