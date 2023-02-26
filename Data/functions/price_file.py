import json
from openpyxl import load_workbook
import os
from datetime import datetime

def pricing_range(current_month):
    if current_month == "January":
        return [7, 10]
    elif current_month == "February":
        return [10, 13]
    elif current_month == "March":
        return [13, 16]
    elif current_month == "April":
        return [16, 19]
    elif current_month == "May":
        return [19, 22]
    elif current_month == "June":
        return [22, 25]
    elif current_month == "July":
        return [25, 28]
    elif current_month == "August":
        return [28, 31]
    elif current_month == "September":
        return [31, 34]
    elif current_month == "October":
        return [34, 37]
    elif current_month == "November":
        return [37, 40]
    elif current_month == "December":
        return [40, 7]
    else:
        return None
    

def update_additions(estimator_id, current_month):
#open estimator.json and return estimator_path using estimator_id
    with open("Data/Keno-bi database/estimator.json", "r") as f:
        estimator_data = json.load(f)
        estimator_path = estimator_data[estimator_id]["estimator_path"] + "\\Price File Additions.xlsx"
        f.close()
#open Price File Additions.xlsx and return the sheet
    wb = load_workbook(estimator_path)
    sheet = wb.active
#Price File Additions.xlsx first row is header, data starts from second row, column A is account_id, column B is product_name, column C is fixed_price
    for row in range(2, sheet.max_row + 1):
        account_id = sheet.cell(row, 1).value
        product_name = sheet.cell(row, 2).value
        fixed_price = sheet.cell(row, 3).value
        #loop through account_id and match the value against account.json key and return the account_path
        with open("Data/Keno-bi database/account.json", "r") as f:
            account_data = json.load(f)
            for key in account_data:
                if key == account_id:
                    account_path = account_data[key]["account_path"]
                    break
            f.close()
        



