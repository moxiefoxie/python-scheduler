# Open DI CDK Partner Vendor Profile Excel Sheet required
# TO DO: Use timestr to get a moving date so the pull is from the last 2 weeks
import csv
import xml.etree.ElementTree as ET
import requests
import time


def opcode():
    # URL from Excel Sheet
    url = 'https://3pa.dmotorworks.com/pip-extract/opcode/extract'
    today = time.strftime("%m/%d/%Y")
    # Get queryId from Excel Sheet
    parameters = {'queryId': 'OPS_Bulk', 'dealerId': '3PA0002255', 'qparamCompany': '1',
                  'qparamStartDate': '07/21/2018', 'qparamEndDate': today}
    r = requests.post(url, params=parameters, auth=('opendi', 'WpmYq0YN2xwq'))

    print(r.url)
    file = open('C:/FTPData/Hardy/XML Files/CBGOpCode.xml', 'w')
    file.write(r.text)
    file.close()
    tree = ET.parse('C:/FTPData/Hardy/XML Files/CBGOpCode.xml')

    root = tree.getroot()
    timestr = time.strftime("%m%d%Y-%H%M%S")
    data = open('C:/FTPData/Hardy/Hardy Chevy Buick GMC/CBGOpCode'+timestr+'.csv', 'w')

    csvwriter = csv.writer(data)
    data_head = []
    count = 0
    #Update the url and namespace
    for member in root.findall("{http://www.dmotorworks.com/pip-extract-opcode}OpCode"):

        items = []
        if count == 0:
            # add data_head.append('Column Name')
            data_head.append('RelatedOpCodes')
            data_head.append('ShopChargeFlagCP')
            data_head.append('ShopChargeFlagWP')
            data_head.append('ShopChargeFlagIP')
            data_head.append('SkillCostingCode')
            data_head.append('OperationType')
            data_head.append('Watched')
            data_head.append('RequiredRelatedOpCodes')
            data_head.append('MLSFlag')
            data_head.append('ItemID')
            data_head.append('Cause')
            data_head.append('ComebackFlag')
            data_head.append('ComplaintCodeFlag')
            data_head.append('CorrectionOpCode')
            data_head.append('Description')
            data_head.append('DiscountFlag')
            data_head.append('DispatchCode')
            data_head.append('Duration')
            data_head.append('EntryDate')
            data_head.append('FlatCostRate')
            data_head.append('FlatHours')
            data_head.append('FlatSellRate')
            data_head.append('GridID')
            data_head.append('ManufacturerCode')
            data_head.append('ManufacturerOpCode')
            data_head.append('ManufacturerOpCodeFlag')
            csvwriter.writerow(data_head)
            count = count + 1

        # Recreate the following two rows for each column; replace the url with the url from the Excel doc
        RelatedOpCodes = member.find('{http://www.dmotorworks.com/pip-extract-opcode}RelatedOpCodes').text
        items.append(RelatedOpCodes)
        ShopChargeFlagCP = member.find('{http://www.dmotorworks.com/pip-extract-opcode}ShopChargeFlagCP').text
        items.append(ShopChargeFlagCP)
        ShopChargeFlagWP = member.find('{http://www.dmotorworks.com/pip-extract-opcode}ShopChargeFlagWP').text
        items.append(ShopChargeFlagWP)
        ShopChargeFlagIP = member.find('{http://www.dmotorworks.com/pip-extract-opcode}ShopChargeFlagIP').text
        items.append(ShopChargeFlagIP)
        SkillCostingCode = member.find('{http://www.dmotorworks.com/pip-extract-opcode}SkillCostingCode').text
        items.append(SkillCostingCode)
        OperationType = member.find('{http://www.dmotorworks.com/pip-extract-opcode}OperationType').text
        items.append(OperationType)
        Watched = member.find('{http://www.dmotorworks.com/pip-extract-opcode}Watched').text
        items.append(Watched)
        RequiredRelatedOpCodes = member.find('{http://www.dmotorworks.com/pip-extract-opcode}RequiredRelatedOpCodes').text
        items.append(RequiredRelatedOpCodes)
        MLSFlag = member.find('{http://www.dmotorworks.com/pip-extract-opcode}MLSFlag').text
        items.append(MLSFlag)
        ItemID = member.find('{http://www.dmotorworks.com/pip-extract-opcode}ItemID').text
        items.append(ItemID)
        Cause = member.find('{http://www.dmotorworks.com/pip-extract-opcode}Cause').text
        items.append(Cause)
        ComebackFlag = member.find('{http://www.dmotorworks.com/pip-extract-opcode}ComebackFlag').text
        items.append(ComebackFlag)
        ComplaintCodeFlag = member.find('{http://www.dmotorworks.com/pip-extract-opcode}ComplaintCodeFlag').text
        items.append(ComplaintCodeFlag)
        CorrectionOpCode = member.find('{http://www.dmotorworks.com/pip-extract-opcode}CorrectionOpCode').text
        items.append(CorrectionOpCode)
        Description = member.find('{http://www.dmotorworks.com/pip-extract-opcode}Description').text
        items.append(Description)
        DiscountFlag = member.find('{http://www.dmotorworks.com/pip-extract-opcode}DiscountFlag').text
        items.append(DiscountFlag)
        DispatchCode = member.find('{http://www.dmotorworks.com/pip-extract-opcode}DispatchCode').text
        items.append(DispatchCode)
        Duration = member.find('{http://www.dmotorworks.com/pip-extract-opcode}Duration').text
        items.append(Duration)
        EntryDate = member.find('{http://www.dmotorworks.com/pip-extract-opcode}EntryDate').text
        items.append(EntryDate)
        FlatCostRate = member.find('{http://www.dmotorworks.com/pip-extract-opcode}FlatCostRate').text
        items.append(FlatCostRate)
        FlatHours = member.find('{http://www.dmotorworks.com/pip-extract-opcode}FlatHours').text
        items.append(FlatHours)
        FlatSellRate = member.find('{http://www.dmotorworks.com/pip-extract-opcode}FlatSellRate').text
        items.append(FlatSellRate)
        GridID = member.find('{http://www.dmotorworks.com/pip-extract-opcode}GridID').text
        items.append(GridID)
        ManufacturerCode = member.find('{http://www.dmotorworks.com/pip-extract-opcode}ManufacturerCode').text
        items.append(ManufacturerCode)
        ManufacturerOpCode = member.find('{http://www.dmotorworks.com/pip-extract-opcode}ManufacturerOpCode').text
        items.append(ManufacturerOpCode)
        ManufacturerOpCodeFlag = member.find('{http://www.dmotorworks.com/pip-extract-opcode}ManufacturerOpCodeFlag').text
        items.append(ManufacturerOpCodeFlag)

        csvwriter.writerow(items)

    data.close()
