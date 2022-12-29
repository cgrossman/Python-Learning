"""
----------------------------------------------------
Author: Chris Grossman

Purpose: The purpose of this script is to extract
the QLik Applications Json from Admin Portal and place
the extract in the database.
-----------------------------------------------------
"""
#import the appropriate the files to be used.
import pandas as pd
import pyodbc as pydb

#This function is meant to be a loop or call that takes the server
#as a variable and captures the JSON from the Admin Portal and then
#places is at as a pandas dataframe.

def GetAppData(server):
    #pass the url to pandas to read the JSON
    #I tried for a few days to get normalize_json to work and it kept coming back empty
    df = pd.read_json("https://qlikap/api/apps/"+server)
    #Rename any of the columns
    #**********************************************************************************
    # App Information
    #**********************************************************************************
    df.rename(columns={
    "id":"AppId"
    ,"name":"AppName"
    ,"description":"AppDescription"
    ,"modifiedDate":"AppModifiedDate"
    ,"modifiedByUserName":"AppModifiedByUserName"
    ,"createdDate":"AppCreatedDate"
    ,"fileSize":"AppFileSize"
    ,"lastReloadTime":"LastReloadTime"
    ,"published":"AppPublished"
    ,"publishTime":"AppPublishTime"
    ,"customProperties":"AppCustomProperties"
    ,"sourceAppId":"SourceAppId"
    ,"targetAppId":"TargetAppId"
    ,"privileges":"AppPrivileges"}, inplace = True)
    #**********************************************************************************
    # Owner Information
    #**********************************************************************************
    #dfOwners = df['owner'].apply(pd.Series)
    df = pd.concat([df['owner'].apply(pd.Series), df.drop('owner',axis=1)], axis=1)
    df.rename(columns={
    "id":"OwnerId"
    ,"userId":"OwnerUserId"
    ,"name":"OwnerName"
    ,"privileges":"OwnerPrivileges"
    ,"userDirectory":"OwnerUserDirectory"
    ,"userDirectoryConnectorName":"OwnerUserDirectoryConnector"
    },inplace=True)
    #**********************************************************************************
    #Stream Information
    #**********************************************************************************
    df = pd.concat([df['stream'].apply(pd.Series), df.drop('stream',axis=1)], axis=1)
    df.rename(columns={
    "id":"StreamId"
    ,"name":"StreamName"
    ,"privileges":"StreamPrivileges"
    },inplace=True)
    #Fill NaN or Missing Stream Values with 0
    df['StreamId'] = df['StreamId'].fillna('No Stream')
    df['StreamName'] = df['StreamName'].fillna('No Stream')
    #Return the full data frame

    conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    #'SERVER=LT171752\SQLEXPRESS;'
    'SERVER=wdpstage1;'
    'Database=QlikAdmin;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()

    for index, row in df.iterrows():
        cursor.execute("INSERT INTO QlikApps (server,AppId,AppOwnerUserId,AppOwner,AppCreatedDate,AppModifiedDate,AppModifiedBy,AppName,AppFileSize,StreamName,StreamId,AppPublished,AppPublishTime,LastReloadTime,InsertDate) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,GETDATE())"
        ,server
        ,row.AppId
        ,row.OwnerUserId
        ,row.OwnerName
        ,row.AppCreatedDate
        ,row.AppModifiedDate
        ,row.AppModifiedByUserName
        ,row.AppName
        ,row.AppFileSize
        ,row.StreamName
        ,row.StreamId
        ,row.AppPublished
        ,row.AppPublishTime
        ,row.LastReloadTime
        )
    conn.commit()
    cursor.close()
    #**********************************************************************************

def InsertNewApps():
    conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    #'SERVER=LT171752\SQLEXPRESS;'
    'SERVER=wdpstage1;'
    'Database=QlikAdmin;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("exec InsertNewApps")
    conn.commit()
    conn.close()

def DeleteApps():
    conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    #'SERVER=LT171752\SQLEXPRESS;'
    'SERVER=wdpstage1;'
    'Database=QlikAdmin;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("exec DeleteApps")
    conn.commit()
    conn.close()

def InsertAppHistory():
    conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    #'SERVER=LT171752\SQLEXPRESS;'
    'SERVER=wdpstage1;'
    'Database=QlikAdmin;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("exec insertapphistory")
    conn.commit()
    conn.close()

#Function to Truncate the QlikApps table
def TruncateAppTable():
    conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    #'SERVER=LT171752\SQLEXPRESS;'
    'SERVER=wdpstage1;'
    'Database=QlikAdmin;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("Truncate table QlikApps")
    conn.commit()
    conn.close()
    
prod='Prod'
dev = 'Dev'
df = GetAppData(prod)
df = GetAppData(dev)