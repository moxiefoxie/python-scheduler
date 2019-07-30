# Open DI CDK Partner Vendor Profile Excel Sheet required
# TO DO: Use timestr to get a moving date so the pull is from the last 2 weeks
import csv
import xml.etree.ElementTree as ET
import requests
import time
from datetime import datetime, timedelta


def salesweekly():
    # URL from Excel Sheet
    url = 'https://3pa.dmotorworks.com/pip-extract/fisales-closed/extract'
    lastweek = datetime.strftime(datetime.now() - timedelta(7), '%m/%d/%Y')
    today = time.strftime("%m/%d/%Y")
    # Get queryId from Excel Sheet
    parameters = {'queryId': 'FISC_DateRange', 'dealerId': '3PA0002255', 'qparamCompany': '1',
                  'qparamStartDate': lastweek, 'qparamEndDate': today}
    r = requests.post(url, params=parameters, auth=('opendi', 'WpmYq0YN2xwq'))

    print(r.url)
    file = open('C:/FTPData/Hardy/XML Files/CBGSalesWeekly.xml', 'w')
    file.write(r.text)
    file.close()
    tree = ET.parse('C:/FTPData/Hardy/XML Files/CBGSalesWeekly.xml')

    root = tree.getroot()
    timestr = time.strftime("%m%d%Y-%H%M%S")
    data = open('C:/FTPData/Hardy/Hardy Chevy Buick GMC/CBGSalesWeekly'+timestr+'.csv', 'w')

    csvwriter = csv.writer(data)
    data_head = []
    count = 0
    # Update the url and namespace
    for member in root.findall("{http://www.dmotorworks.com/pip-extract-fisales-closed}FISalesClosed"):

        items = []
        if count == 0:
            # add data_head.append('Column Name')
            data_head.append('StockNo')
            data_head.append('SalesDate')
            data_head.append('FIDealType')
            data_head.append('Year')
            data_head.append('Make')
            data_head.append('Model')
            data_head.append('Salesperson1')
            data_head.append('Salesperson2')
            data_head.append('DealType')
            data_head.append('VIN')
            data_head.append('BackGross')
            data_head.append('FrontGross')
            data_head.append('TotalGross')
            data_head.append('GrossProfit')
            csvwriter.writerow(data_head)
            count = count + 1

        # Recreate the following two rows for each column; replace the url with the url from the Excel doc
        StockNo = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}StockNo').text
        items.append(StockNo)
        SalesDate = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}SalesDate').text
        items.append(SalesDate)
        FIDealType = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}FIDealType').text
        items.append(FIDealType)
        Year = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}Year').text
        items.append(Year)
        Make = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}Make').text
        items.append(Make)
        Model = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}Model').text
        items.append(Model)
        Salesperson1 = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}Salesperson1').text
        items.append(Salesperson1)
        Salesperson2 = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}Salesperson2').text
        items.append(Salesperson2)
        DealType = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}DealType').text
        items.append(DealType)
        VIN = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}VIN').text
        items.append(VIN)
        BackGross = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}BackGross').text
        items.append(BackGross)
        FrontGross = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}FrontGross').text
        items.append(FrontGross)
        TotalGross = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}TotalGross').text
        items.append(TotalGross)
        GrossProfit = member.find('{http://www.dmotorworks.com/pip-extract-fisales-closed}GrossProfit').text
        items.append(GrossProfit)

        csvwriter.writerow(items)

    data.close()
