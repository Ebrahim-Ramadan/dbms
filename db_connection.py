import pyodbc

connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=SHARMOWUVESJOJI\SQLEXPRESS;'
    'DATABASE=uni;'
    'Trusted_Connection=yes;'
)

try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
def get_db_connection():
    return pyodbc.connect(connection_string)