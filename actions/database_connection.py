import pyodbc 
import pandas as pd

def database_connection():
    cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=192.168.1.126;"
            "Database=Bigdata;"
            "Trusted_Connection=yes;"
           "UID=sa;"
            "PWD=123456$i;")
    cnxn = pyodbc.connect(cnxn_str)
    return cnxn.cursor()