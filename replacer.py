import json
import ovh

oldIP = "XXX.XXX.XXX.XXX"  # Replace with your old IP
newIP = "XXX.XXX.XXX.XXX"  # Replace with your new IP

client = ovh.Client(
    endpoint='ovh-eu',
    application_key='XXXXXXXXXXXXXXXXXXX',                  # Application Key
    application_secret='XXXXXXXXXXXXXXXXXXX',               # Application Secret
    consumer_key='XXXXXXXXXXXXXXXXXXX',                     # Consumer Key
)

domainNames = client.get('/domain/zone')
domainRecords = {}
domainIP = {}

for x in domainNames:
    link = '/domain/zone/' + x + '/record'
    try:
       domainRecords[x] = client.get(link)
    except:
       print("Domain expired!")

for x in domainRecords:
    saveID = []
    for y in domainRecords[x]:
        link = '/domain/zone/' + x + '/record/' + str(y)
        result = client.get(link)
        if result["target"] == oldIP:
            saveID.append(y)
    domainIP[x] = saveID



for x in domainIP:
    for y in domainIP[x]:
        link = '/domain/zone/' + x + '/record/' + str(y)
        result = client.put(link, 
            target=newIP
        )

for x in domainIP:
    link = '/domain/zone/' + x + '/refresh'
    result = client.post(link)
