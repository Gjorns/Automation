import os
import json
from Data.functions.menu import *

def check_account_name(account_name):
    with open("Data/Keno-bi database/account.json", "r") as f:
        account_data = json.load(f)
        for account_id in account_data:
            if account_data[account_id]['account_name'] == account_name:
                return True
    return False

def check_account_id(account_id):
    with open("Data/Keno-bi database/account.json", "r") as f:
        account_data = json.load(f)
        if account_id in account_data:
            return True
    return False

def create_new_price_file(estimator_id):
    if not check_estimator_id(estimator_id):
        print(f"Error: Estimator ID {estimator_id} not found")
        return

    with open("Data/Keno-bi database/general.json", "r") as f:
        general_data = json.load(f)
        nacet_path = general_data['nacet']

    while True:
        account_id = input("Enter Account ID (or type 'exit' to cancel): ").strip().upper()
        if account_id == 'EXIT':
            return
        if check_account_id(account_id):
            print(f"Error: Account ID '{account_id}' already exists")
            continue

        account_name = input("Enter Account name (or type 'exit' to cancel): ").strip().title()
        if account_name == 'EXIT':
            return
        if check_account_name(account_name):
            print(f"Error: Account name '{account_name}' already exists")
            continue

        print("Select Account Vertical:")
        print("1. New Build")
        print("2. Social Housing")
        print("3. Private & Domestic")
        while True:
            account_vertical = input("(Enter a number or type 'exit' to cancel): ").strip()
            if account_vertical == '1':
                account_vertical = 'New Build'
                break
            elif account_vertical == '2':
                account_vertical = 'Social Housing'
                break
            elif account_vertical == '3':
                account_vertical = 'Private & Domestic'
                break
            elif account_vertical.lower() == 'exit':
                return
            else:
                print("Invalid input, please try again")

        print("Select Account Type:")
        print("1. SLP")
        print("2. MARGIN")
        while True:
            account_type = input("(Enter a number or type 'exit' to cancel): ").strip()
            if account_type == '1':
                account_type = 'SLP'
                break
            elif account_type == '2':
                account_type = 'MARGIN'
                break
            elif account_type.lower() == 'exit':
                return
            else:
                print("Invalid input, please try again")

        account_mngr_firstname = input("Enter Account Manager first name (or type 'exit' to cancel): ").strip().capitalize()
        if account_mngr_firstname == 'Exit':
            return

        account_mngr_lastname = input("Enter Account Manager last name (or type 'exit' to cancel): ").strip().capitalize()
        if account_mngr_lastname == 'exit':
            return

        print("Does account have copper file? (Y/N):")
        while True:
            copper_file = input("(Enter 'Y' or 'N', or type 'exit' to cancel): ").strip().upper()
            if copper_file == 'Y':
                copper_file = True
                break
            elif copper_file == 'N':
                copper_file = False
                break
            elif copper_file == 'exit':
                return
            else:
                print("Invalid input, please try again")

        account_owner = estimator_id

        account_dir_path = os.path.join(nacet_path, "accounts", account_vertical, account_name)
        account_file_path = os.path.join(nacet_path, "accounts", account_vertical, account_name, f"{account_id} - {account_name} master.xlsx")

        os.makedirs(account_dir_path, exist_ok=True)

        with open("Data/Keno-bi database/account.json", "r") as f:
            account_data = json.load(f)

        account_data[account_id] = {
            "account_name": account_name,
            "account_vertical": account_vertical,
            "account_type": account_type,
            "account_mngr_firstname": account_mngr_firstname,
            "account_mngr_lastname": account_mngr_lastname,
            "copper_file": copper_file,
            "account_owner": account_owner,
            "account_file_path": account_file_path
        }

        with open("Data/Keno-bi database/account.json", "w") as f:
            json.dump(account_data, f, indent=4)

        print(f"New account '{account_name}' with ID '{account_id}' has been created!")
        return
    
def list_all_accounts(estimator_id):
    with open('Data/Keno-bi database/estimator.json') as f:
        accounts = json.load(f)
    
    matches = []
    for account_id, account in accounts.items():
        if account['account_owner'] == estimator_id:
            matches.append((account_id, account['account_name'], account['account_vertical'], account['account_type']))
    
    if len(matches) > 0:
        print("Matches found for estimator with ID", estimator_id)
        print("---------------------------------------------------")
        print(f"{'ID':<10} {'Account Name':<20} {'Vertical':<20} {'Type':<20}")
        print("---------------------------------------------------")
        for match in matches:
            print(f"{match[0]:<10} {match[1]:<20} {match[2]:<20} {match[3]:<20}")
    else:
        print("No matches found for estimator with ID", estimator_id)
    
    input("Press Enter to continue...")