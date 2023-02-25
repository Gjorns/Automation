import os
import shutil
import json

def create_new_estimator():
    with open("Data/Keno-bi database/general.json", "r") as f:
        general_data = json.load(f)
        nacet_path = general_data['nacet']
        templates_path = general_data['templates']

    while True:
        first_name = input("Enter first name (or type 'exit' to cancel): ").strip().capitalize()
        if first_name == 'exit':
            return
        last_name = input("Enter last name (or type 'exit' to cancel): ").strip().capitalize()
        if last_name == 'exit':
            return

        estimator_id = f"{first_name[0]}{last_name[0]}"
        estimator_path = os.path.join(nacet_path, "Estimators", f"{first_name} {last_name}")

        with open("Data/Keno-bi database/estimator.json", "r") as f:
            estimator_data = json.load(f)

        if estimator_id in estimator_data:
            print(f"Error: Estimator ID {estimator_id} already exists")
        else:
            estimator_data[estimator_id] = {
                "first_name": first_name,
                "last_name": last_name,
                "estimator_path": estimator_path
            }

            with open("Data/Keno-bi database/estimator.json", "w") as f:
                json.dump(estimator_data, f, indent=4)

            if not os.path.exists(estimator_path):
                os.makedirs(estimator_path)
                # Add Price File Additions.xlsx to new estimator directory
                price_file_additions_path = os.path.join(templates_path, "Price File Additions.xlsx")
                estimator_price_file_path = os.path.join(estimator_path, "Price File Additions.xlsx")
                shutil.copy(price_file_additions_path, estimator_price_file_path)
                print(f"New Estimator '{first_name} {last_name}' with ID '{estimator_id}' has been created!")
            else:
                estimator_price_file_path = os.path.join(estimator_path, "Price File Additions.xlsx")
                if not os.path.exists(estimator_price_file_path):
                    # Add Price File Additions.xlsx to existing estimator directory
                    price_file_additions_path = os.path.join(templates_path, "Price File Additions.xlsx")
                    shutil.copy(price_file_additions_path, estimator_price_file_path)
                    print(f"Price File Additions.xlsx has been added to '{first_name} {last_name}' estimator directory.")
                else:
                    print(f"Directory '{estimator_path}' and 'Price File Additions.xlsx' already exist.")
            return

def delete_estimator():
    estimator_id = input("Enter estimator ID to delete: ").strip().upper()

    with open("Data/Keno-bi database/estimator.json", "r") as f:
        estimator_data = json.load(f)

    if estimator_id in estimator_data:
        estimator_info = estimator_data[estimator_id]
        print(f"Are you sure you want to delete estimator {estimator_id}: {estimator_info['first_name']} {estimator_info['last_name']}?")

        while True:
            choice = input("Enter Y to delete or N to cancel: ").strip().lower()

            if choice == 'y':
                del estimator_data[estimator_id]

                with open("Data/Keno-bi database/estimator.json", "w") as f:
                    json.dump(estimator_data, f, indent=4)

                print(f"Estimator {estimator_id} has been successfully deleted!")
                break

            elif choice == 'n':
                print(f"Estimator {estimator_id} deletion has been cancelled!")
                break

            else:
                print("Invalid choice. Please try again.")
                continue

    else:
        print(f"Error: Estimator ID {estimator_id} not found")


def list_all_estimators():
    with open('Data/Keno-bi database/estimator.json', 'r') as f:
        estimator_data = json.load(f)
    for key in estimator_data:
        firstname = estimator_data[key]['first_name']
        lastname = estimator_data[key]['last_name']
        print(f"{key} - {firstname} {lastname}")
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')