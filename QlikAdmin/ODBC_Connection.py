conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    #'SERVER=LT171752\SQLEXPRESS;'
    'SERVER=wdtstage1;'
    'Database=QlikAdmin;'
    'Trusted_Connection=yes;')
cursor = conn.cursor()