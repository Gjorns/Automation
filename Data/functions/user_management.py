import json
import os

def create_new_estimator():
    with open("Data/Keno-bi database/general.json", "r") as f:
        general_data = json.load(f)
        nacet_path = general_data['nacet']

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
            else:
                print(f"Directory '{estimator_path}' already exists.")

            print(f"New Estimator '{first_name} {last_name}' with ID '{estimator_id}' has been created!")
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
    with open("Data/Keno-bi database/estimator.json", "r") as f:
        estimator_data = json.load(f)
    
    print("List of All Estimators:")
    print("-----------------------")
    print("ID\tName")
    print("-----------------------")
    
    for estimator_id, data in estimator_data.items():
        estimator_name = data["estimator_name"]
        print(f"{estimator_id}\t{estimator_name}")
    
    input("Press Enter to continue...")
