import os
import json

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nMAIN MENU")
    print("---------")
    print("1. Estimator")
    print("2. User Management")
    print("3. Reports")
    print("0. Exit")

def estimator_menu(estimator_id):
    if not check_estimator_id(estimator_id):
        print(f"Error: Estimator ID {estimator_id} not found")
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\nWelcome, {estimator_id}!")
    print("\nESTIMATOR MENU")
    print("--------------")
    print("1. Update Additions")
    print("2. Update Price Files")
    print("3. Create new Price File")
    print("4. List all Accounts")
    print("0. Back (to main menu)")

def user_management_menu(estimator_id):
    if not check_estimator_id(estimator_id):
        print(f"Error: Estimator ID {estimator_id} not found")
        return
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\nWelcome, {estimator_id}!")
    print("\nUSER MANAGEMENT MENU")
    print("--------------------")
    print("1. Create new Estimator")
    print("2. Remove Estimator")
    print("3. List all Estimators")
    print("0. Back (to main menu)")

def reports_menu(estimator_id):
    if not check_estimator_id(estimator_id):
        print(f"Error: Estimator ID {estimator_id} not found")
        return
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\nWelcome, {estimator_id}!")
    print("\nREPORTS MENU")
    print("------------")
    print("1. Report Option A")
    print("2. Report Option B")
    print("0. Back (to main menu)")

def check_estimator_id(estimator_id):
    with open("Data/Keno-bi database/estimator.json", "r") as f:
        account_data = json.load(f)
        if estimator_id.upper() in account_data:
            return True
        else:
            return False