import json
import openpyxl

def export_accounts():
    # Load account data from JSON file
    with open('Data/Keno-bi database/account.json', 'r') as f:
        account_data = json.load(f)

    # Create a new Excel workbook and worksheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Write header row to worksheet
    worksheet.append(["Key", "Account Name", "Account Vertical", "Account Type",
                      "Account Manager First Name", "Account Manager Last Name",
                      "Copper File", "Account Owner", "Account File Path"])

    # Write account data to worksheet
    for key in account_data:
        row = [key]
        for field in account_data[key].values():
            row.append(field)
        worksheet.append(row)

    # Save workbook to file
    workbook.save('Reports/accounts_export.xlsx')

    print("Accounts data exported to Reports/accounts_export.xlsx")
    input("Press Enter to continue...")

def export_estimators():
    # Load estimator data from JSON file
    with open('Data/Keno-bi database/estimator.json', 'r') as f:
        estimator_data = json.load(f)

    # Create a new Excel workbook and worksheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Write header row to worksheet
    worksheet.append(["Key", "First Name", "Last Name", "Estimator Path"])

    # Write estimator data to worksheet
    for key in estimator_data:
        row = [key]
        for field in estimator_data[key].values():
            row.append(field)
        worksheet.append(row)

    # Save workbook to file
    workbook.save('Reports/estimators_export.xlsx')

    print("Estimators data exported to Reports/estimators_export.xlsx")
    input("Press Enter to continue...")