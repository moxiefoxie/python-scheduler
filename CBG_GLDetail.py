# Open DI CDK Partner Vendor Profile Excel Sheet required
# TO DO: Use timestr to get a moving date so the pull is from the last 2 weeks
import csv
import xml.etree.ElementTree as ET
import requests
import time
from datetime import datetime, timedelta

def gldetail():
    # URL from Excel Sheet
    url = 'https://3pa.dmotorworks.com/pip-extract/gl-je-detail/extract'
    today = time.strftime("%m/%d/%Y")
    # Get queryId from Excel Sheet
    parameters = {'queryId': 'ACCTGL_JE_DateRange_D', 'dealerId': '3PA0002255', 'qparamCompany': '1',
                  'qparamStartDate': '07/21/2018', 'qparamEndDate': today}
    r = requests.post(url, params=parameters, auth=('opendi', 'WpmYq0YN2xwq'))

    print(r.url)
    file = open('C:/FTPData/Hardy/XML Files/CBGGLDetails.xml', 'w')
    file.write(r.text)
    file.close()
    tree = ET.parse('C:/FTPData/Hardy/XML Files/CBGGLDetails.xml')

    root = tree.getroot()
    timestr = time.strftime("%m%d%Y-%H%M%S")
    data = open('C:/FTPData/Hardy/Hardy Chevy Buick GMC/CBGGLDetails'+timestr+'.csv', 'w')

    csvwriter = csv.writer(data)
    data_head = []
    count = 0
    #Update the url and namespace
    for member in root.findall("{http://www.dmotorworks.com/pip-extract-accounting-gl}GLJEDetail"):

        items = []
        if count == 0:
            # add data_head.append('Column Name')
            data_head.append('Control')
            data_head.append('JournalID')
            data_head.append('AccountingDate')
            data_head.append('DetailDescription')
            data_head.append('AccountNumber')
            data_head.append('PostingAmount')
            data_head.append('Refer')
            csvwriter.writerow(data_head)
            count = count + 1

        # Recreate the following two rows for each column; replace the url with the url from the Excel doc
        Control = member.find('{http://www.dmotorworks.com/pip-extract-accounting-gl}Control').text
        items.append(Control)
        JournalID = member.find('{http://www.dmotorworks.com/pip-extract-accounting-gl}JournalID').text
        items.append(JournalID)
        AccountingDate = member.find('{http://www.dmotorworks.com/pip-extract-accounting-gl}AccountingDate').text
        items.append(AccountingDate)
        DetailDescription = member.find('{http://www.dmotorworks.com/pip-extract-accounting-gl}DetailDescription').text
        items.append(DetailDescription)
        AccountNumber = member.find('{http://www.dmotorworks.com/pip-extract-accounting-gl}AccountNumber').text
        items.append(AccountNumber)
        PostingAmount = member.find('{http://www.dmotorworks.com/pip-extract-accounting-gl}PostingAmount').text
        items.append(PostingAmount)
        Refer = member.find('{http://www.dmotorworks.com/pip-extract-accounting-gl}Refer').text
        items.append(Refer)

        csvwriter.writerow(items)

    data.close()
