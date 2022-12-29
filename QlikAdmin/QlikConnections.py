"""
----------------------------------------------------
Author: Chris Grossman

Purpose: The purpose of this script is to extract
the QLik Connections Json from Admin Portal and place
the extract in the database.
-----------------------------------------------------
"""

#import the appropriate the files to be used.
import pandas as pd
import pyodbc as pydb

#The url is already doing the api call and returns the Json

def GetConnections(server):
    #Parse JSON as Dataframe
    df = pd.read_json("https://qlikap/api/dataconnections?server="+server)

    #************** Rename Connection Dataframe Columns ****#
    df.rename(columns={
    "id":"ConnectionId"
    ,"createdDate":"CreatedDate"
    ,"modifiedDate":"ModifiedDate"
    ,"modifiedByUserName":"ModifiedByUserName"
    ,"name":"Connection"
    ,"connectionstring":"ConnectionString"
    ,"type":"ConnectionType"
    ,"engineObjectId":"EngineObjectId"
    ,"username":"UserName"
    ,"password":"Password"
    ,"logOn":"LogOn"
    ,"architecture":"Architecture"
    ,"privileges":"ConnPrivileges"
    ,"schemaPath":"ConnSchemaPath"}, inplace = True)
    #**********************************************************************************
    # Owner Information
    #**********************************************************************************
    dfOwners = df['owner'].apply(pd.Series)
    df = pd.concat([df['owner'].apply(pd.Series), df.drop('owner',axis=1)], axis=1)
    df.rename(columns={
    "id":"OwnerId"
    ,"userId":"OwnerUserId"
    ,"name":"OwnerName"
    ,"privileges":"OwnerPrivileges"
    ,"userDirectory":"OwnerUserDirectory"
    ,"userDirectoryConnectorName":"OwnerUserDirectoryConnector"
    },inplace=True)

    #*************** Connnect To Database *****************#
    conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=wdpstage1;'
    'Database=QlikAdmin;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    #cursor.execute("truncate table QlikConnections")

    for index, row in df.iterrows():
        cursor.execute("INSERT INTO QlikConnections (Server,[OwnerId],[OwnerUserId],[OwnerUserDirectory],[OwnerName],[ConnectionId],[Connection],[CreatedDate],[ModifiedDate],[ModifiedByUserName],[ConnectionString],[ConnectionType],[UserName],[Password],InsertDate) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,GETDATE())"
        ,server
        ,row.OwnerId
        ,row.OwnerUserId
        ,row.OwnerUserDirectory
        ,row.OwnerName
        ,row.ConnectionId
        ,row.Connection
        ,row.CreatedDate
        ,row.ModifiedDate
        ,row.ModifiedByUserName
        ,row.ConnectionString
        ,row.ConnectionType
        ,row.UserName
        ,row.Password
        )
    conn.commit()
    cursor.close()

def TruncateConnectionTable():
    conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    #'SERVER=LT171752\SQLEXPRESS;'
    'SERVER=wdtstage1;'
    'Database=QlikAdmin;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("Truncate table QlikConnections")
    conn.commit()
    conn.close()


prod = 'prod'
dev = 'dev'
GetConnections(prod)
GetConnections(dev)

