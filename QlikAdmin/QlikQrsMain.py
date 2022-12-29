# This is going to be the main program. Tried to plan it out so that each file was
# it's own process and then I can 
#
#import QlikApplications as app
import QlikConnections as conn
#import QlikTasks as task

prod='prod'
dev = 'dev'
#------------- APPLICATIONS ---------------------
#Truncate Table
#app.TruncateAppTable()
#--Get Application data
#app.GetAppData(prod)
#app.GetAppData(dev)
#--Function that will call a stored procedure so we can see new created apps
#app.InsertNewApps()
#--Funtion that will call a stored procedure to identify apps that were deleted
#app.DeleteApps()
#--Insert rows for history
#app.InsertAppHistory()

#------------- CONNECTIONS ----------------------
#Truncate Table
conn.TruncateConnectionTable()
#Insert rows for connections
conn.GetConnections(prod)
conn.GetConnections(dev)
#Connection History

#------------- TASKS ----------------------------
#Truncate Task table
#task.TruncateTasksTable()
#Insert fors for Tasks
#task.GetTasks(prod)
#task.GetTasks(dev)