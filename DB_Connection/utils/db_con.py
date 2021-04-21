import pyodbc


class Connect:
    def __init__(self, server_name, db_name):
        self.server_name = server_name
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = pyodbc.connect(Trusted_Connection='Yes', driver='{SQL Server}', server=self.server_name, database=self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()





