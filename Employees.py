# Open DI CDK Partner Vendor Profile Excel Sheet required
# TO DO: Use timestr to get a moving date so the pull is from the last 2 weeks
import csv
import xml.etree.ElementTree as ET
import requests
import time


def employees():
    # URL from Excel Sheet
    url = 'https://3pa.dmotorworks.com/pip-extract/help-employee/extract'

    # Get queryId from Excel Sheet
    parameters = {'queryId': 'HEMPL_Bulk_Service', 'dealerId': '3PA0002255', 'qparamCompany': '5',
                  'qparamStartDate': '07/21/2019', 'qparamEndDate': '07/23/2019'}
    r = requests.post(url, params=parameters, auth=('opendi', 'WpmYq0YN2xwq'))

    print(r.url)
    file = open('C:/Users/swith/Documents/employees.xml', 'w')
    file.write(r.text)
    file.close()
    tree = ET.parse('C:/Users/swith/Documents/employees.xml')

    root = tree.getroot()
    timestr = time.strftime("%m%d%Y-%H%M%S")
    data = open('C:/Users/swith/Documents/employees'+timestr+'.csv', 'w')

    csvwriter = csv.writer(data)
    data_head = []
    count = 0

    #Update the url and namespace
    for member in root.findall("{http://www.dmotorworks.com/pip-extract-help-employee}HelpEmployee"):

        items = []
        if count == 0:
            # add data_head.append('Column Name')
            data_head.append('ID')
            data_head.append('Name')
            csvwriter.writerow(data_head)
            count = count + 1

        # Recreate the following two rows for each column; replace the url with the url from the Excel doc
        Id = member.find('{http://www.dmotorworks.com/pip-extract-help-employee}Id').text
        items.append(Id)
        Name = member.find('{http://www.dmotorworks.com/pip-extract-help-employee}Name').text
        items.append(Name)

        csvwriter.writerow(items)

    data.close()
