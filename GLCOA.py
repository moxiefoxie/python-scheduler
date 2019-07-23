import csv
import xml.etree.ElementTree as ET
import requests
import time
url = 'https://3pa.dmotorworks.com/pip-extract/gl-coa/extract'
parameters = {'queryId': 'ACCTGL_COA_Bulk', 'dealerId': '3PA0002255', 'qparamCompany': '5',
              'qparamStartDate': '07/21/2019', 'qparamEndDate': '07/23/2019'}
r = requests.post(url, params=parameters, auth=('opendi', 'WpmYq0YN2xwq'))

print(r.url)
file = open('C:/Users/swith/Documents/data.xml', 'w')
file.write(r.text)
file.close()
tree = ET.parse('C:/Users/swith/Documents/data.xml')

root = tree.getroot()
timestr = time.strftime("%m%d%Y-%H%M%S")
data = open('C:/Users/swith/Documents/glcoa'+timestr+'.csv', 'w')

csvwriter = csv.writer(data)
data_head = []
count = 0
for member in root.findall("{http://www.dmotorworks.com/pip-extract-accounting-gl}GLCOA"):

    glcoa = []
    if count == 0:
        #accountDesc = member.find('{http://www.dmotorworks.com/pip-extract-accounting-gl}AccountDescription').tag
        data_head.append('Account Description')
        csvwriter.writerow(data_head)
        count = count + 1

    accountDesc = member.find('{http://www.dmotorworks.com/pip-extract-accounting-gl}AccountDescription').text
    glcoa.append(accountDesc)
    csvwriter.writerow(glcoa)
data.close()
