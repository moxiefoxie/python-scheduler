# Open DI CDK Partner Vendor Profile Excel Sheet required
# TO DO: Use timestr to get a moving date so the pull is from the last 2 weeks
import csv
import xml.etree.ElementTree as ET
import requests
import time

def salesinstall():
    # URL from Excel Sheet
    url = 'https://3pa.dmotorworks.com/pip-extract/fisaleshistory/extract'
    today = time.strftime("%m/%d/%Y")
    # Get queryId from Excel Sheet
    parameters = {'queryId': 'FISH_DateRange', 'dealerId': '3PA0002255', 'qparamCompany': '5',
              'qparamStartDate': '07/21/2018', 'qparamEndDate': today}
    r   = requests.post(url, params=parameters, auth=('opendi', 'WpmYq0YN2xwq'))

    print(r.url)
    file = open('C:/FTPData/Hardy/XML Files/FFSalesWeekly.xml', 'w')
    file.write(r.text)
    file.close()
    tree = ET.parse('C:/FTPData/Hardy/XML Files/FFSalesWeekly.xml')

    root = tree.getroot()
    timestr = time.strftime("%m%d%Y-%H%M%S")
    data = open('C:/FTPData/Hardy/Family Ford/FFSalesWeekly'+timestr+'.csv', 'w')

    csvwriter = csv.writer(data)
    data_head = []
    count = 0
    #Update the url and namespace
    for member in root.findall("{http://www.dmotorworks.com/pip-extract-fisales-history}FISalesHistory"):

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
    StockNo = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}StockNo').text
    items.append(StockNo)
    SalesDate = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}SalesDate').text
    items.append(SalesDate)
    FIDealType = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}FIDealType').text
    items.append(FIDealType)
    Year = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}Year').text
    items.append(Year)
    Make = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}Make').text
    items.append(Make)
    Model = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}Model').text
    items.append(Model)
    Salesperson1 = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}Salesperson1').text
    items.append(Salesperson1)
    Salesperson2 = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}Salesperson2').text
    items.append(Salesperson2)
    DealType = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}DealType').text
    items.append(DealType)
    VIN = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}VIN').text
    items.append(VIN)
    BackGross = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}BackGross').text
    items.append(BackGross)
    FrontGross = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}FrontGross').text
    items.append(FrontGross)
    TotalGross = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}TotalGross').text
    items.append(TotalGross)
    GrossProfit = member.find('{http://www.dmotorworks.com/pip-extract-fisales-history}GrossProfit').text
    items.append(GrossProfit)

    csvwriter.writerow(items)
    data.close()