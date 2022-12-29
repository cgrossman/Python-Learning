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

def GetTasks(server):
    #Parse JSON as Dataframe
    df = pd.read_json("https://qlikap/api/tasks/"+server)
    df.rename(columns={
    "id":"TaskId"
    ,"name":"TaskName"
    ,"taskType":"TaskType"
    ,"enabled":"TaskEnabled"
    ,"taskSessionTimeout":"TaskSessionTimeout" 
    ,"privileges":"TaskPrivileges"   
    }, inplace = True)
    #**********************************************************************************
    #Task Operation Information - Rename some columns for easier inserts
    #**********************************************************************************
    df = pd.concat([df['operational'].apply(pd.Series), df.drop('operational',axis=1)], axis=1)
    df.rename(columns={
    "id":"OperationId"
    ,"lastExecutionResult":"LastExecutionResult"
    ,"nextExecution":"NextExecution"
    ,"privileges":"OperationPrivileges"
    ,"taskSessionTimeout":"TaskSessionTimeout" 
    ,"privileges":"TaskPrivileges"   
    }, inplace = True)
    #lastExecutionResult
    df = pd.concat([df['LastExecutionResult'].apply(pd.Series), df.drop('LastExecutionResult',axis=1)], axis=1)
    df.rename(columns={
    "executingNodeName":"ExecutionNode"
    ,"status":"Status"
    ,"startTime":"StartTime"
    ,"stopTime":"StopTime" 
    ,"duration":"Duration"
    ,"privileges":"LastExecutedTaskPrivileges"   
    ,"fileReferenceID":"FileReferenceId"
    ,"scriptLogAvailable":"ScriptLogAvailable"
    ,"scriptLogSize":"ScriptLogSize"
    ,"details":"Details"
    ,"scriptLogLocation":"ScriptLogLocation"
    }, inplace = True)

    conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=wdpstage1;'
    'Database=QlikAdmin;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()

    for index, row in df.iterrows():
        cursor.execute("INSERT INTO QlikTasks (server,TaskId,TaskName,TaskType,TaskEnabled,TaskSessionTimeout,Status,StartTime,StopTime,Duration,NextExecution,ExecutionNode,ScriptLogLocation,ScriptLogSize,InsertDate) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,GETDATE())"
        ,server
        ,row.TaskId
        ,row.TaskName
        ,row.TaskType
        ,row.TaskEnabled
        ,row.TaskSessionTimeout
        ,row.Status
        ,row.StartTime
        ,row.StopTime
        ,row.Duration
        ,row.NextExecution
        ,row.ExecutionNode
        ,row.ScriptLogLocation
        ,row.ScriptLogSize
        )
    conn.commit()
    cursor.close()

def TruncateTasksTable():
    conn = pydb.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    #'SERVER=LT171752\SQLEXPRESS;'
    'SERVER=wdpstage1;'
    'Database=QlikAdmin;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("Truncate table QlikTasks")
    conn.commit()
    conn.close()

#prod = 'Prod'
#GetTasks(prod)