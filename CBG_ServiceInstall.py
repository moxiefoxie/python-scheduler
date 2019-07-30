# Open DI CDK Partner Vendor Profile Excel Sheet required
# TO DO: Use timestr to get a moving date so the pull is from the last 2 weeks
import csv
import xml.etree.ElementTree as ET
import requests
import time
# import lxml.etree as ET

# URL from Excel Sheet
url = 'https://3pa.dmotorworks.com/pip-extract/service-ro-closed/extract'
today = time.strftime("%m/%d/%Y")
# Get queryId from Excel Sheet
parameters = {'queryId': 'SROD_Closed_DateRange', 'dealerId': '3PA0002255', 'qparamCompany': '1',
              'qparamStartDate': '07/21/2018', 'qparamEndDate': today}
r = requests.post(url, params=parameters, auth=('opendi', 'WpmYq0YN2xwq'))

print(r.url)
file = open('C:/FTPData/Hardy/XML Files/CBGservice2.xml', 'w')
file.write(r.text)
file.close()
tree = ET.parse('C:/FTPData/Hardy/XML Files/CBGservice2.xml')

root = tree.getroot()
timestr = time.strftime("%m%d%Y-%H%M%S")
data = open('C:/FTPData/Hardy/Hardy Chevy Buick GMC/CBGservice'+timestr+'.csv', 'w')

csvwriter = csv.writer(data)
data_head = []
count = 0
# Update the url and namespace
for member in root.findall("{http://www.dmotorworks.com/pip-extract-service-ro-history}service-repair-order-history"):

    items = []
    if count == 0:
        # add data_head.append('Column Name')
        data_head.append('Multivalue Count')
        data_head.append('Comeback Flag')
        data_head.append('Booker No')
        data_head.append('')
        data_head.append('')
        data_head.append('')
        data_head.append('')
        data_head.append('')
        data_head.append('')
        data_head.append('')
        data_head.append('')
        data_head.append('')

        csvwriter.writerow(data_head)
        count = count + 1

    # Recreate the following two rows for each column; replace the url with the url from the Excel doc
    mvc = member.find('{http://www.dmotorworks.com/pip-extract-service-ro-history}dedMultivalueCount').text
    items.append(mvc)
    cbf = member.find('{http://www.dmotorworks.com/pip-extract-service-ro-history}lbrComebackFlag').text
    items.append(cbf)
    bn = member.find('{http://www.dmotorworks.com/pip-extract-service-ro-history}linBookerNo').text
    items.append(bn)
#    = member.find('{http://www.dmotorworks.com/pip-extract-service-ro-history}').text
#    items.append()
#   = member.find('{http://www.dmotorworks.com/pip-extract-service-ro-history}').text
    # items.append()
    # = member.find('{http://www.dmotorworks.com/pip-extract-service-ro-history}').text
#    items.append()
#   = member.find('{http://www.dmotorworks.com/pip-extract-service-ro-history}').text
#  items.append()
# = member.find('{http://www.dmotorworks.com/pip-extract-service-ro-history}').text
#   items.append()

    csvwriter.writerow(items)

data.close()