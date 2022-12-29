#This is going to be a script that will connect directly to the QRS API.
import requests
import pandas as pd
import pyodbc as pydb

requests.packages.urllib3.disable_warnings()

#Set up necessary headers comma separated
xrf = 'iX83QmNlvu87yyAB'
headers = {'X-Qlik-xrfkey': xrf,
"Content-Type": "application/json",
"X-Qlik-User":"UserDirectory=INTERNAL;UserId=sa_repository"}

#Set up the certificate path
cert = 'C:\Cert\Qlik\ClientAndKey.pem'

url = 'https://wrdqlik01.ds.ohnet:4242/qrs/systemrule/full?xrfkey={}'.format(xrf)

#Call the endpoint to get the list of Qlik Sense apps
resp = requests.get(url, headers=headers, verify=False, cert=cert)

#The the response and convert it to a Pandas DataFrame.
df = pd.DataFrame(resp.json())

#changing the name of the column 'name' as it's a keyword and inserting wrong data
df.rename(columns={"name":"rulename"}, inplace = True)

conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
#'SERVER=LT171752\SQLEXPRESS;'
'SERVER=wdpstage1;'
'Database=QlikAdmin;'
'Trusted_Connection=yes;')

cursor = conn.cursor()
for index, row in df.iterrows():
    cursor.execute("INSERT INTO QlikSecurityRules ([server],[id],[createdDate],[modifiedDate],[modifiedByUserName],[type],[name],[rule],[resourceFilter],[comment],[disabled],[seedId],[schemaPath],[InsertDateTime]) values('Dev',?,?,?,?,?,?,?,?,?,?,?,?,GETDATE())"
    ,row.id
    ,row.createdDate
    ,row.modifiedDate
    ,row.modifiedByUserName
    ,row.type
    ,row.rulename
    ,row.rule
    ,row.resourceFilter
    ,row.comment
    ,row.disabled
    ,row.seedId
    ,row.schemaPath)

conn.commit()
cursor.close()