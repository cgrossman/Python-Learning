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

userid = '100214'

#Set the endpoint URL
url = 'https://wrdqlik01.ds.ohnet:4242/qrs/user/?id={}&xrfkey={}'.format(xrf)

#Call the endpoint to get the list of Qlik Sense apps
resp = requests.delete(url, headers=headers, verify=False, cert=cert)
