# Open DI CDK Partner Vendor Profile Excel Sheet required
# TO DO: Use timestr to get a moving date so the pull is from the last 2 weeks
import csv
import xml.etree.ElementTree as ET
import requests
import time
from datetime import datetime, timedelta
# URL from Excel Sheet
url = ''
lastweek = datetime.strftime(datetime.now() - timedelta(7), '%m/%d/%Y')
today = time.strftime("%m/%d/%Y")
# Get queryId from Excel Sheet
parameters = {'queryId': '', 'dealerId': '3PA0002255', 'qparamCompany': '5',
              'qparamStartDate': '07/21/2019', 'qparamEndDate': today}
r = requests.post(url, params=parameters, auth=('opendi', 'WpmYq0YN2xwq'))

print(r.url)
file = open('C:/FTPData/Hardy/XML Files/FFservice.xml', 'w')
file.write(r.text)
file.close()
tree = ET.parse('C:/FTPData/Hardy/XML Files/FFservice.xml')

root = tree.getroot()
timestr = time.strftime("%m%d%Y-%H%M%S")
data = open('C:/FTPData/Hardy/Family Ford/FFservice'+timestr+'.csv', 'w')

csvwriter = csv.writer(data)
data_head = []
count = 0
#Update the url and namespace
for member in root.findall("{http://www.dmotorworks.com/pip-extract-accounting-gl}GLCOA"):

    items = []
    if count == 0:
        # add data_head.append('Column Name')
        data_head.append('Account Description')

        csvwriter.writerow(data_head)
        count = count + 1

    # Recreate the following two rows for each column; replace the url with the url from the Excel doc
    accountDesc = member.find('{http://www.dmotorworks.com/pip-extract-accounting-gl}AccountDescription').text
    items.append(accountDesc)

    csvwriter.writerow(items)

data.close()