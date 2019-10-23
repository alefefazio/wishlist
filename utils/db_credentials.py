import os

class DBCredentials():

    credentials = {}

    def __init__(self):

        self.credentials = {
            "dbname":os.environ["dbname"],
            "user":os.environ["user"],
            "password":os.environ["password"],
            "host":os.environ["host"],
            "port":os.environ["port"],
        }