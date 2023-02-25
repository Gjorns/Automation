from Data.functions.menu import *
from Data.functions.user_management import *
from Data.functions.accounts_management import *


estimator_id = ""

while True:
    main_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        if not estimator_id:
            estimator_id = input("Enter your Estimator ID: ")
            if not check_estimator_id(estimator_id):
                input("Press Enter to continue...")
                estimator_id = ""
                continue

        while True:
            estimator_menu(estimator_id)
            estimator_choice = input("Enter your choice: ")
            if estimator_choice == "1":
                update_additions()
            elif estimator_choice == "2":
                update_price_files()
            elif estimator_choice == "3":
                create_new_price_file(estimator_id)
            elif estimator_choice == "4":
                list_all_accounts(estimator_id)
            elif estimator_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")
    elif choice == "2":
        if not estimator_id:
            estimator_id = input("Enter your Estimator ID: ")
            if not check_estimator_id(estimator_id):
                input("Press Enter to continue...")
                estimator_id = ""
                continue

        while True:
            user_management_menu(estimator_id)
            user_choice = input("Enter your choice: ")
            if user_choice == "1":
                create_new_estimator()
            elif user_choice == "2":
                delete_estimator()
            elif user_choice == "3":
                list_all_estimators()
            elif user_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")
    elif choice == "3":
        if not estimator_id:
            estimator_id = input("Enter your Estimator ID: ")
            if not check_estimator_id(estimator_id):
                input("Press Enter to continue...")
                estimator_id = ""
                continue

        while True:
            reports_menu(estimator_id)
            reports_choice = input("Enter your choice: ")
            if reports_choice == "1":
                report_option_a()
            elif reports_choice == "2":
                report_option_b()
            elif reports_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")

